import ast
from datetime import datetime

from django.db import transaction
from tastypie import fields
from tastypie.exceptions import BadRequest
from tastypie.resources import ModelResource
from django.contrib.auth.models import User

from OPENiapp.APIS.Context.models import OpeniContext
from OPENiapp.Providers.generic import execution
from OPENiapp.APIS.permissions import Permissions


__author__ = 'amertis'


class ContextAwareResource(ModelResource):
    from OPENiapp.APIS.Context.Resources import ContextResource

    context = fields.ToOneField(ContextResource, 'context', full=True)

    # TODO remove this only to openigenericresource
    def cbs_handling(self, request, **kwargs):

        pathSplit = request.path.split('/')

        pathSplitLength = len(pathSplit)
        version = pathSplit[1]
        resource_name = pathSplit[2].lower()
        id = ""
        connection = ""
        if pathSplitLength > 3:
            id = pathSplit[3]
            if pathSplitLength > 4:
                connection = pathSplit[4].lower()

        params = ""
        for each in request.REQUEST.dicts[1]:
            if each != 'user' and each != 'api_key' and each != 'cbs' and each != 'limit' and each != 'offset':
                params = request.REQUEST.dicts[1]

        # Try to parse the parameters of the call
        try:
            user = request.GET.get("user")
            u = User.objects.filter(username=user)
        except:
            # To-Do: Make an appropriate error response!
            return [{"error": "User is not authenticated. Please refer to the documentation"}]

        # Try to get the cbs required for the call
        try:
            cbs = ast.literal_eval(request.GET.get("cbs"))
        except:
            return [{"CBS": "Only Cloudlet Objects were retrieved. No additional CBS were selected."}]

        # Try to parse the parameters of the call
        #try:
        #    params = ast.literal_eval(request.GET.get("params"))
        #except:
        #    params = ""

        request_method = request.META['REQUEST_METHOD'].lower()
        method = request_method + '_' + resource_name
        # print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
        # print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
        # print request_method
        # print resource_name
        # print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
        # print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
        # print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
        if not Permissions(request).permissions_verified(method=request_method,object_type=resource_name):
            return {"Permissions are not verified for the specific request."}
        # If there is a connection in the url then add it to the method
        if connection != "":
            method += '_' + connection
            # If there is an id in the url then make the methods plural.
        if id == "":
            if (resource_name == 'status'):
                method += 'e'
            if (resource_name != 'rsvp'):
                method += 's'

        executable = execution(u, cbs, method, id, params)
        return executable.make_all_connections()

    @transaction.atomic
    def obj_create(self, bundle, **kwargs):
        bundle = self.full_hydrate(bundle)

        try:
            if bundle.request.GET.get("cbs"):
                cbs_return = self.cbs_handling(bundle.request, **kwargs)
            #else:
            #    raise AttributeError
            #return self.create_response(bundle.request, cbs_return)
        except:
            pass

        if bundle.obj.context is None:
            raise BadRequest("context attribute is not defined")
        bundle.obj.context.save()
        bundle.obj.context_id = bundle.obj.context.id
        bundle.obj.save()
        bundle.obj.context.objectid = bundle.obj.id
        # bundle.obj.context.save(update_fields=["objectid"])
        bundle.obj.context.save()

        # dynamic attributes generation
        bundle.obj.context = self.populate_dynamic_attributes(bundle.obj.context)
        bundle.obj.context.save()

        return bundle

    def populate_dynamic_attributes(self, context_bundle):
        properties = {
            "location": ["latitude", "longitude", "height", "dynamic_creation_date", "dynamic_ted", "dynamic_uncertainty_weight", "dynamic_information_source", "dynamic_mechanism_obtained", "dynamic_information_methodology"],
            "time": ["created", "edited", "deleted", "dynamic_creation_date", "dynamic_ted", "dynamic_uncertainty_weight", "dynamic_information_source", "dynamic_mechanism_obtained", "dynamic_information_methodology"],
            "duration": ["time_started", "time_ended", "dynamic_creation_date", "dynamic_ted", "dynamic_uncertainty_weight", "dynamic_information_source", "dynamic_mechanism_obtained", "dynamic_information_methodology"],
            "address": ["street", "number", "apartment", "city", "locality", "country", "zip", "dynamic_creation_date", "dynamic_ted", "dynamic_uncertainty_weight", "dynamic_information_source", "dynamic_mechanism_obtained", "dynamic_information_methodology"],
            "current_location": ["latitude", "longitude", "height", "time","dynamic_creation_date", "dynamic_ted", "dynamic_uncertainty_weight", "dynamic_information_source", "dynamic_mechanism_obtained", "dynamic_information_methodology"],
            "rating": ["value", "dynamic_creation_date", "dynamic_ted", "dynamic_uncertainty_weight", "dynamic_information_source", "dynamic_mechanism_obtained", "dynamic_information_methodology"],
            "mood": ["value", "dynamic_creation_date", "dynamic_ted", "dynamic_uncertainty_weight", "dynamic_information_source", "dynamic_mechanism_obtained", "dynamic_information_methodology"],
            "device": ["wireless_network_type", "wireless_channel_quality", "accelerometers", "cell_log", "sms_log", "call_log",
                       "running_applications", "installed_applications", "screen_state", "battery_status", "dynamic_creation_date", "dynamic_ted", "dynamic_uncertainty_weight", "dynamic_information_source", "dynamic_mechanism_obtained", "dynamic_information_methodology"],
            "application": ["background_color", "format", "font", "color", "background", "text", "box", "classification",
                            "text_copy", "dynamic_creation_date", "dynamic_ted", "dynamic_uncertainty_weight", "dynamic_information_source", "dynamic_mechanism_obtained", "dynamic_information_methodology"],
            "personalization": ["age_range", "country", "postal_code", "region", "town", "roaming", "opt_out", "carrier",
                                "handset", "user_ids", "device_id", "application_id", "device_type", "device_os", "gender",
                                "has_children", "ethnicity", "income", "household_size", "education", "interests",
                                "customer_tag",
                                "users_language", "dynamic_creation_date", "dynamic_ted", "dynamic_uncertainty_weight", "dynamic_information_source", "dynamic_mechanism_obtained", "dynamic_information_methodology"],
            "community": ["list", "dynamic_creation_date", "dynamic_ted", "dynamic_uncertainty_weight", "dynamic_information_source", "dynamic_mechanism_obtained", "dynamic_information_methodology"],
        }

        for var in properties:
            is_empty = True
            ted = var+"_dynamic_ted"
            method = var+"_dynamic_information_methodology"
            source = var+"_dynamic_information_source"
            mechanism = var+"_dynamic_mechanism_obtained"
            creation_date = var+"_dynamic_creation_date"

            for cat_attr in properties[var]:
                if getattr(context_bundle, var+"_"+cat_attr) is not None:
                    is_empty = False
                    if "time" == var:
                        if getattr(context_bundle, ted) is None:
                            setattr(context_bundle, ted, "MT")
                        if getattr(context_bundle, method) is None:
                            setattr(context_bundle, method, "Direct")
                        if getattr(context_bundle, source) is None:
                            setattr(context_bundle, source, "System")
                        if getattr(context_bundle, mechanism) is None:
                            setattr(context_bundle, mechanism, "Static")
                    elif "duration" == var:
                        if getattr(context_bundle, ted) is None:
                            setattr(context_bundle, ted, "MT")
                        if getattr(context_bundle, method) is None:
                            setattr(context_bundle, method, "Direct")
                        if getattr(context_bundle, source) is None:
                            setattr(context_bundle, source, "System")
                        if getattr(context_bundle, mechanism) is None:
                            setattr(context_bundle, mechanism, "Derived")
                    elif "location" == var:
                        if getattr(context_bundle, ted) is None:
                            setattr(context_bundle, ted, "ST")
                        if getattr(context_bundle, method) is None:
                            setattr(context_bundle, method, "Direct")
                        if getattr(context_bundle, source) is None:
                            setattr(context_bundle, source, "System")
                        if getattr(context_bundle, mechanism) is None:
                            setattr(context_bundle, mechanism, "Sensed")
                    elif "address" == var:
                        if getattr(context_bundle, ted) is None:
                            setattr(context_bundle, ted, "LT")
                        if getattr(context_bundle, method) is None:
                            setattr(context_bundle, method, "Indirect")
                        if getattr(context_bundle, source) is None:
                            setattr(context_bundle, source, "Application")
                        if getattr(context_bundle, mechanism) is None:
                            setattr(context_bundle, mechanism, "Static")
                    elif "current_location" == var:
                        if getattr(context_bundle, ted) is None:
                            setattr(context_bundle, ted, "ST")
                        if getattr(context_bundle, method) is None:
                            setattr(context_bundle, method, "Indirect")
                        if getattr(context_bundle, source) is None:
                            setattr(context_bundle, source, "System")
                        if getattr(context_bundle, mechanism) is None:
                            setattr(context_bundle, mechanism, "Sensed")
                    elif "rating" == var:
                        if getattr(context_bundle, ted) is None:
                            setattr(context_bundle, ted, "ST")
                        if getattr(context_bundle, method) is None:
                            setattr(context_bundle, method, "Indirect")
                        if getattr(context_bundle, source) is None:
                            setattr(context_bundle, source, "Application")
                        if getattr(context_bundle, mechanism) is None:
                            setattr(context_bundle, mechanism, "Derived")
                    elif "mood" == var:
                        if getattr(context_bundle, ted) is None:
                            setattr(context_bundle, ted, "ST")
                        if getattr(context_bundle, method) is None:
                            setattr(context_bundle, method, "Indirect")
                        if getattr(context_bundle, source) is None:
                            setattr(context_bundle, source, "Application")
                        if getattr(context_bundle, mechanism) is None:
                            setattr(context_bundle, mechanism, "Derived")
                    elif "device" == var:
                        if getattr(context_bundle, ted) is None:
                            setattr(context_bundle, ted, "F")
                        if getattr(context_bundle, method) is None:
                            setattr(context_bundle, method, "Direct")
                        if getattr(context_bundle, source) is None:
                            setattr(context_bundle, source, "System")
                        if getattr(context_bundle, mechanism) is None:
                            setattr(context_bundle, mechanism, "Static")
                    elif "application" == var:
                        if getattr(context_bundle, ted) is None:
                            setattr(context_bundle, ted, "F")
                        if getattr(context_bundle, method) is None:
                            setattr(context_bundle, method, "Direct")
                        if getattr(context_bundle, source) is None:
                            setattr(context_bundle, source, "Application")
                        if getattr(context_bundle, mechanism) is None:
                            setattr(context_bundle, mechanism, "Static")
                    elif "personalization" == var:
                        if getattr(context_bundle, ted) is None:
                            setattr(context_bundle, ted, "ST")
                        if getattr(context_bundle, method) is None:
                            setattr(context_bundle, method, "Indirect")
                        if getattr(context_bundle, source) is None:
                            setattr(context_bundle, source, "Application")
                        if getattr(context_bundle, mechanism) is None:
                            setattr(context_bundle, mechanism, "Derived")
                    elif "community" == var:
                        if getattr(context_bundle, ted) is None:
                            setattr(context_bundle, ted, "MT")
                        if getattr(context_bundle, method) is None:
                            setattr(context_bundle, method, "Indirect")
                        if getattr(context_bundle, source) is None:
                            setattr(context_bundle, source, "Application")
                        if getattr(context_bundle, mechanism) is None:
                            setattr(context_bundle, mechanism, "Derived")

                    break
            if is_empty:
                setattr(context_bundle, var+"_dynamic_uncertainty_weight", self.calculate_uncertainty(True, "", "", "", ""))
            else:
                setattr(context_bundle, var+"_dynamic_uncertainty_weight", self.calculate_uncertainty(False,
                                                getattr(context_bundle, ted), getattr(context_bundle, source),
                                                getattr(context_bundle, mechanism), getattr(context_bundle, method)))
            setattr(context_bundle, creation_date, datetime.now())
        return context_bundle

    def calculate_uncertainty(self, empty, dynamic_ted, dynamic_information_source, dynamic_mechanism_obtained,
                              dynamic_information_methodology):

        from random import randint
        import math

        mech_low_rand = float(randint(0, 30))/100
        mech_med_rand = float(randint(30, 60))/100
        mech_high_rand = float(randint(60, 100))/100

        source_low_rand = float(randint(0, 35))/100
        source_high_rand = float(randint(35, 100))/100

        method_low_rand = float(randint(0, 30))/100
        method_high_rand = float(randint(30, 100))/100

        ted_low_rand = float(randint(0, 25))/100
        ted_med_low_rand = float(randint(25, 50))/100
        ted_med_high_rand = float(randint(50, 75))/100
        ted_high_rand = float(randint(75, 100))/100

        uncertainty = 0

        if empty:
            return float(100)
        else:
            if dynamic_mechanism_obtained == 'Static':
                uncertainty += mech_low_rand * 50
            elif dynamic_mechanism_obtained == 'Sensed':
                uncertainty += mech_med_rand * 50
            elif dynamic_mechanism_obtained == 'Derived':
                uncertainty += mech_high_rand * 50
            else:
                uncertainty += 50

            if dynamic_information_source == 'System':
                uncertainty += source_low_rand * 25
            elif dynamic_information_source == 'Application':
                uncertainty += source_high_rand * 25
            else:
                uncertainty += 25

            if dynamic_information_methodology == 'Direct':
                uncertainty += method_low_rand * 20
            elif dynamic_information_methodology == 'Indirect':
                uncertainty += method_high_rand * 20
            else:
                uncertainty += 20

            if dynamic_ted == 'F':
                uncertainty += ted_low_rand * 5
            elif dynamic_ted == 'FT':
                uncertainty += ted_med_low_rand * 5
            elif dynamic_ted == 'MT':
                uncertainty += ted_med_high_rand * 5
            elif dynamic_ted == 'ST':
                uncertainty += ted_high_rand * 5
            else:
                uncertainty += 5

            if uncertainty == 0:
                return float(100)
            else:
                return math.ceil(uncertainty)

    @transaction.atomic
    def obj_update(self, bundle, **kwargs):

        try:
            if bundle.request.GET.get("cbs"):
                cbs_return = self.cbs_handling(bundle.request, **kwargs)
            #else:
            #    raise AttributeError
            #return self.create_response(bundle.request, cbs_return)
        except:
            pass

        if 'id' not in bundle.data:
            raise BadRequest("id property not found")
        bundle = self.full_hydrate(bundle)
        if bundle.obj.context.id is None:
            raise BadRequest("context id not found")
        bundle.obj.context = self.populate_dynamic_attributes(bundle.obj.context)
        bundle.obj.context.save()
        bundle.obj.save()
        return bundle

        # def obj_delete(self, bundle, **kwargs):
    #     return bundle
    @transaction.atomic
    def obj_delete(self, bundle, **kwargs):

        try:
            if bundle.request.GET.get("cbs"):
                cbs_return = self.cbs_handling(bundle.request, **kwargs)
            #else:
            #    raise AttributeError
            #return self.create_response(bundle.request, cbs_return)
        except:
            pass

        if 'pk' not in kwargs:
            raise BadRequest("no pk parameter found")
        try:
            pk = int(kwargs['pk'])
        except ValueError, e:
            raise BadRequest("invalid pk parameter")
        bundle = self.full_hydrate(bundle)
        type(bundle.obj).objects.filter(id=pk).delete()
        OpeniContext.objects.filter(objectid=pk).delete()
        return bundle
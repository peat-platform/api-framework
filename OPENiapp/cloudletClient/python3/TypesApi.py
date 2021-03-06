#!/usr/bin/env python
"""
WordAPI.py
Copyright 2014 Wordnik, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os

from .models import *


class TypesApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    

    def createType(self, body, **kwargs):
        """Creates a type.

        Args:
            body, OPENiType: The type to be created. (required)

            

        Returns: CreateResponse
        """

        allParams = ['body']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createType" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/types'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CreateResponse')
        return responseObject
        

        

    def createTypes(self, body, **kwargs):
        """Create multiple types in a single request.

        Args:
            body, list[OPENiType]: JSON array of the types to be created. (required)

            

        Returns: Array[CreateResponse]
        """

        allParams = ['body']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createTypes" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/types'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PATCH'

        queryParams = {}
        headerParams = {}

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Array[CreateResponse]')
        return responseObject
        

        

    def getTypes(self, **kwargs):
        """Retrieves the OPENi types on the system.

        Args:
            skip, int: Pagination feature, the amount of objects to skip. (optional)

            limit, int: The amount of objects to return. (optional)

            id_only, bool: If true returns an array of object ids instead of the full objects. (optional)

            content-type, str: Supported content-type is application/json-ld. (optional)

            

        Returns: Array[OPENiType]
        """

        allParams = ['skip', 'limit', 'id_only', 'content-type']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTypes" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/types'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('skip' in params):
            queryParams['skip'] = self.apiClient.toPathValue(params['skip'])
        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])
        if ('id_only' in params):
            queryParams['id_only'] = self.apiClient.toPathValue(params['id_only'])
        if ('content-type' in params):
            queryParams['content-type'] = self.apiClient.toPathValue(params['content-type'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Array[OPENiType]')
        return responseObject
        

        

    def getType(self, typeID, **kwargs):
        """Get a type.

        Args:
            typeID, str: The Id of the type. (required)

            content-type, str: Supported content-type is application/json-ld. (optional)

            

        Returns: OPENiType
        """

        allParams = ['typeID', 'content-type']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getType" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/types/{typeID}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('content-type' in params):
            queryParams['content-type'] = self.apiClient.toPathValue(params['content-type'])
        if ('typeID' in params):
            replacement = str(self.apiClient.toPathValue(params['typeID']))
            resourcePath = resourcePath.replace('{' + 'typeID' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'OPENiType')
        return responseObject
        

        

    def getStats(self, **kwargs):
        """Retrieves the Types usage stats.

        Args:
            

        Returns: Array[Stat]
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getStats" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/types/stats'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Array[Stat]')
        return responseObject
        

        

    





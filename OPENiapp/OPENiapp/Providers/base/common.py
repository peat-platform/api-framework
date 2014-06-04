defJsonRes = "Doesn't Exist"
defaultMethodResponse = "Not supported by this service"

def check_if_exists(data, check, otherwise = defJsonRes):
    """ Loop through the  """
    checkArray = check.split('.')
    ret = data
    for allChecks in checkArray:
        if hasattr(ret, allChecks):
            ret = getattr(ret, allChecks)
        elif isinstance(ret, (list, dict)) and (allChecks in ret):
            ret = ret[allChecks]
        else:
            return otherwise
    return ret

def format_file(file_title, file_description, file_format, file_size, file_icon):
    return {
                "title": file_title,
                "description": file_description,
                "format": file_format,
                "size": file_size,
                "icon": file_icon
            }

def format_person(from_id, from_name, from_surname, from_middlename, from_birthdate, from_orgs):
    return {
                "id": from_id,
                "name": from_name,
                "surname": from_surname,
                "middlename": from_middlename,
                "birthdate": from_birthdate,
                "organizations": from_orgs
            }

def format_time(created_time, edited_time, deleted_time):
    return {
                "created_time": created_time,
                "edited_time": edited_time,
                "deleted_time": deleted_time
            }

def format_location(location_latitude, location_longtitude, location_height):
    return {
                "latitude": location_latitude,
                "longtitude": location_longtitude,
                "height": location_height
            }

def format_tags(data):
    return {
                "id": data['id'],
                "name": data['name'],
                "time":
                    { "created_time": data['time_created_time'],
                      "edited_time": data['time_edited_time'],
                      "deleted_time": data['time_deleted_time']
                    },
                "x-location": data['x-location'],
                "y-location": data['y-location']
            }
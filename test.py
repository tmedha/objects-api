import service as s
from pprint import pp

if __name__ == "__main__":
    # pp(s.get_all_objects())
    # s.delete_all_objects()
    # id = s.add_object({
    #     "name":"Param",
    #     "data": {
    #         "use": "tutor",
    #         "personality": "amazing"
    #     }
    # })
    # pp(s.delete_object(1))
    # pp(s.get_object(1))
    s.place_object(30,{
        "name": "lamborghini chalai jaane o",
        "type" : 1234
    })
    pp(s.get_all_objects())
    pp(s.modify_object(30, {
        "quality": "bad"
    }))
    pp(s.modify_object(24,{
        "use":"nothing"
    }))
    pp(s.get_all_objects())
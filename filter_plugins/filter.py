class FilterModule(object):
    def filters(self):
        return {
            'search_id': self.search_id,
}
    def search_id(self, custom_dict, value='Identity'):
        for i in custom_dict:
            if i['name'] == value:
                return i['id']
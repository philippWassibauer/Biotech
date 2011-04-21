def dump_cms_data():
    local('./manage.py dumpdata cms text picture link file snippet googlemap mptt menus publisher --indent 4 > fixtures/cms.json')

def load_cms_data():
    local("./manage.py loaddata fixtures/cms.json")

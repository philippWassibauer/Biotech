def dump_cms_data():
    local('./manage.py dumpdata cms text picture link file snippet googlemap mptt menus publisher --indent 4 > fixtures/cms.json')

def load_cms_data():
    local("./manage.py loaddata fixtures/cms.json")



def makemessages():
    makedbmessages() #this will pull fields out of db into python object, where they are picked up by the next call
    local('./manage.py makemessages -a -e ".html, .txt"')


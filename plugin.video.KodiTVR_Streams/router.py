# hack to be able to test code from terminal
class FillPlugin:
    def route(self):
        def decorator(func):
            return func
        return decorator

PLUGIN = FillPlugin

try:
    import routing
    PLUGIN = routing.Plugin()
except:
    pass

def path_for_provider(key):
    return "/providers/%s" % key

def path_for_source(key):
    return "/sources/%s" % key

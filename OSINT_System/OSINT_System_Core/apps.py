from django.apps import AppConfig


class OsintSystemCoreConfig(AppConfig):
    name = 'OSINT_System_Core'
    def ready(self):
        
        print('...................{0}...........Initiated .................'.format(self.name))
        from OSINT_System_Core.digger_control import Digger
        try:
            from OSINT_System_Core.digger_control import Digger
            digger = Digger(10)
            digger.daemon = True
            digger.start()

        except (KeyboardInterrupt,SystemExit):
            digger.done()
            print('.............................Digger Turned OFF...........................')
            

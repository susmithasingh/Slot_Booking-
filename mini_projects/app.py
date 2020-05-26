from django.apps import AppConfig

class MiniProjectsAppConfig(AppConfig):
    name = "mini_projects"

    def ready(self):
        from mini_projects import signals # pylint: disable=unused-variable

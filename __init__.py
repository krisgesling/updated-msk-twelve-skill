from mycroft import MycroftSkill, intent_file_handler


class UpdatedMskTwelve(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('twelve.msk.updated.intent')
    def handle_twelve_msk_updated(self, message):
        self.speak_dialog('twelve.msk.updated')


def create_skill():
    return UpdatedMskTwelve()


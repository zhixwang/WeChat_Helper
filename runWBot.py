from wBot import WBot


def run(Activate_voice_helper = False):
    rob = WBot(Activate_voice_helper)
    rob.run()

if __name__ == '__main__':
    run(False)

    #run(True): activate voice helper; in other cases, deactivate
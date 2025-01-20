import pygame
class Settings:
    @staticmethod
    def readRaw():
        userSettings = {}
        with open('settings.ini', 'r+') as settings:
            for setting in settings: 
                setting = setting.strip().split('=')
                userSettings[setting[0]] = setting[1]

        return userSettings

    @staticmethod
    def getSettings():
        settings = Settings.readRaw()

        resolution = settings['resolution'].split(',')
        resolution = (int(resolution[0]), int(resolution[1]))
        settings['resolution'] = resolution

        if (settings['display'] == 'fullscreen'):
            settings['display'] = pygame.FULLSCREEN
        elif (settings['display'] == 'windowed'):
            settings['display'] = 0


        return settings



    @staticmethod
    def set(key, value): 
        settings = Settings.readRaw()
        settings[key] = value 

        updatedSettingsStr = '' 

        for key in settings.keys():
            updatedSettingsStr += key + '=' + settings[key] + '\n'

        with open('settings.ini', 'w') as settings:
            settings.write(updatedSettingsStr)

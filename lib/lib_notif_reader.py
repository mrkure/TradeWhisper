from winrt.windows.ui.notifications.management import UserNotificationListener
from winrt.windows.ui.notifications import NotificationKinds, KnownNotificationBindings
import asyncio
import time, datetime, time, re
from datetime import datetime

class MyNotification:
    # strings = ['Microsoft Teams', 'Outlook', 'Software Center']
    def __init__(self, time_raw, app, raw_strings):
        self.time_raw, self.app, self.raw_strings = time_raw, app, raw_strings
        self.sender, self.title, self.message = '','', ''
        self.find = re.compile('.?(?=S přátelskými)')

    def get_time(self, time_epoch):
        tt = int(time_epoch * 10e-8) 
        tt2 = datetime.fromtimestamp(tt)
        tt3 = datetime(tt2.year -369, tt2.month, tt2.day, tt2.hour, tt2.minute, tt2.second)
        tt4 = tt3.strftime("%Y.%m.%d, %H:%M:%S")
        return tt4.strip()
    
    def evaluate(self):
        self.time = self.get_time(self.time_raw)
            
        if self.app == 'Microsoft Teams':
            self.title   = ''
            if 'posted a new message' in self.sender:
                for num, string in enumerate(self.raw_strings):
                    if num == 0:
                        self.message = string if len(string) < 40 else string[0:40] + '...'
                    elif num == 1:
                        self.sender  = string
            else:    
                for num, string in enumerate(self.raw_strings):
                    if num == 0:
                        self.sender  = string
                    if num == 1:
                        self.message = string if len(string) < 40 else string[0:40] + '...'

        elif self.app == 'Outlook':
            for num, string in enumerate(self.raw_strings):
                if num == 0:
                    self.sender  = string
                elif num == 1:
                    self.title   = string
                elif num == 2:
                    self.message = re.split(self.find,string)[0][0:40] + '...'
                            
        else:
            for num, string in enumerate(self.raw_strings):
                if num == 0:
                    self.title  = string
                elif num == 1:
                    self.message   = string if len(string) < 40 else string[0:40] + '...'
 

    def printt(self):
        print('Date and time:       ', self.time)
        print("From application:    ", self.app)  
        print("Notification sender: ", self.sender)
        print("Notification title:  ", self.title)
        print('Message:             ', self.message)
        print('======================================================')     
            
class MyNotificatons:
    def __init__(self):
        self.notifications = []
        self.notif_times = []
        self.last_time_notif = -1
    def evaluate_notifications(self):
        for notification in self.notifications:
            notification.evaluate()
            self.notif_times.append(notification.time_raw)
        self.notif_times.sort()
        if len(self.notif_times):
            self.last_time_notif = self.notif_times[-1]
        
    def clear_notifications(self):
        self.notifications = []
        self.notif_times = []
            
    def printt(self):
        for notification in self.notifications:
            notification.printt()
        # print(self.last_time_notif)

            
class NotificationReader:    
    listener  = UserNotificationListener.get_current()
    last_time_checked = None
    
    def __init__(self):       
        self.listener.request_access_async()

    async def notifications_reading(self, exclude_apps, from_time, my_notifications):
        notifications = await self.listener.get_notifications_async(NotificationKinds.TOAST)

        for notif in notifications:     
            text_sequence = notif.notification.visual.get_binding(KnownNotificationBindings.get_toast_generic()).get_text_elements()
            iterator      = iter(text_sequence)
            notif_time    = notif.creation_time.universal_time.real
            notif_app     = notif.app_info.display_info.display_name.strip()
            
            if notif_time <= from_time:
                continue         
            if any(notif_app == app for app in exclude_apps):
                continue

            raw_strings   = []
            
            raw_strings.append(iterator.current.text.strip())
            for x in range(5):
                next(iterator, None)
                if iterator.has_current:
                    notification_text = iterator.current.text
                    raw_strings.append(iterator.current.text.strip())
                else:
                    break
            
            my_notifications.notifications.append(MyNotification(notif_time, notif_app, raw_strings))
            
    def read_notifications(self, from_apps, from_time, my_notifications):
        asyncio.run(self.notifications_reading(from_apps, from_time, my_notifications))

def current_win_epoch_stamp():
    unix_epoch    = datetime(1970, 1, 1)
    windows_epoch = datetime(1601, 1, 1)
    diff          = unix_epoch - windows_epoch
    
    unix_now    = datetime.now()
    windows_now = unix_now + diff
    
    windows_now_stamp = datetime.timestamp(windows_now)
    windows_now_stamp = int(str(windows_now_stamp).replace('.','')+'0' )
    return windows_now_stamp
  
# print(current_win_epoch_stamp())
#%% MAIN

# if __name__ == "__main__":
#     exclude_apps = ['Microsoft Teams']
#     from_apps = []
#     from_time = None
#     my_notifications = MyNotificatons()
#     my_notifications.last_time_notif = current_win_epoch_stamp()
#     notif_reader     = NotificationReader()
#     # notif_reader.read_notifications(from_apps, my_notifications.last_time_notif, my_notifications)
#     # my_notifications.evaluate_notifications()
#     # my_notifications.printt()
    
# while True:
#     notif_reader.read_notifications(from_apps, my_notifications.last_time_notif, my_notifications)
#     my_notifications.evaluate_notifications()
#     my_notifications.printt()
#     my_notifications.clear_notifications()
#     # print('--------------NEXT ITERATION--------------------')
#     time.sleep(5)
    
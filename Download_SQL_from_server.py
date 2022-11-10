# -!- coding: utf-8 -!-
# read data once from SQL - import data to CSV files

import mysql.connector as connection
import pandas as pd

try:

  #connect to the DB
  mydb = connection.connect(
  host="database-1.chnkyqgv9zhg.eu-central-1.rds.amazonaws.com",
  user="User",
  password="PLEASE INSERT PASSWORD",
  database="TAU_Maya")

  # Aware Device; Connect label with Questionnaire
  query_Aware_And_Questionnaire = """SELECT AD.label, AD.device_id, PQ.*
                    FROM aware_device AD JOIN Personality_Q_Alteryx PQ on AD.label=PQ.Email;"""


  #df_Aware = pd.read_sql(query_Aware_And_Questionnaire, mydb)
  #df_Aware.to_csv("MySQL_output\Aware_And_Questionnaire_csv.csv")
  # Aware Device; Connect label with Questionnaire - manualy (Maya's research only)
  df_Aware = pd.read_csv('MySQL_output\Aware_Maya.csv')
  df_Q = pd.read_csv('MySQL_output\Q_Maya.csv')
  df_merge = df_Q.merge(df_Aware, left_on='Email', right_on='label', left_index=False, right_index=False)
  df_merge.to_csv("MySQL_output\Aware_And_Questionnaire_csv.csv")
  #print(df_merge)


  # Bluetooth
  query_Bluetooth = """select device_id ,Date(from_unixtime(timestamp/1000)) as date, count( DISTINCT bt_name) as count,
            CASE 
            WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 0 AND 6 THEN 'PART_1'
            WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 6 AND 12 THEN 'PART_2'
            WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 12 AND 18 THEN 'PART_3'
            WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 18 AND 24 THEN 'PART_4'
            END as part_of_the_day
            from bluetooth b2
            group by device_id, part_of_the_day, date
    ;"""
  #df_Bluetooth = pd.read_sql(query_Bluetooth,mydb)
  #df_Bluetooth.to_csv("MySQL_output\Bluetooth_csv.csv")
  query_Bluetooth_week = """select device_id, count( DISTINCT bt_name) as count
              from bluetooth b2
              group by device_id
      ;"""
  #df_Bluetooth_week = pd.read_sql(query_Bluetooth_week,mydb)
  #df_Bluetooth_week.to_csv("MySQL_output\Bluetooth_week_csv.csv")

  query_Battery='''SELECT device_id , Date(from_unixtime(timestamp/1000)) as date, battery_start,
                        CASE 
                        WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 0 AND 6 THEN 'PART_1'
                        WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 6 AND 12 THEN 'PART_2'
                        WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 12 AND 18 THEN 'PART_3'
                        WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 18 AND 24 THEN 'PART_4'
                        END as part_of_the_day
                        from battery_charges bc
                        '''
  #df_Battery = pd.read_sql(query_Battery,mydb)
  #df_Battery.to_csv("MySQL_output\Battery_csv.csv")
  #print(df_Battery)

  #Calls
  #Raw date
  query_Calls='''SELECT device_id , Date(from_unixtime(timestamp/1000)) as date , call_type, call_duration,trace,
                  CASE 
                  WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 0 AND 6 THEN 'PART_1'
                  WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 6 AND 12 THEN 'PART_2'
                  WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 12 AND 18 THEN 'PART_3'
                  WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 18 AND 24 THEN 'PART_4'
                  END as part_of_the_day
                  from calls c;'''
  #df_calls = pd.read_sql(query_Calls,mydb)
  #df_calls.to_csv("MySQL_output\Calls_csv.csv")

  #AVG num of calls per part of the day (1/2/3) Per user per type
  query_num_calls='''select device_id ,date,call_type, count(call_type) as counter, part_of_the_day
                  from (
                  SELECT device_id , Date(from_unixtime(timestamp/1000)) as date , hour(from_unixtime(timestamp/1000)) AS hour , call_type,
                  CASE 
                  WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 0 AND 6 THEN 'PART_1'
                  WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 6 AND 12 THEN 'PART_2'
                  WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 12 AND 18 THEN 'PART_3'
                  WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 18 AND 24 THEN 'PART_4'
                  END as part_of_the_day
                  from calls c) as sub
                  group by device_id, date, part_of_the_day, call_type'''
  #df_num_calls = pd.read_sql(query_num_calls,mydb)
  #df_num_calls.to_csv("MySQL_output\Calls_num_csv.csv")

  #Average call duration without type 3 (missed calls)
  query_duration_calls='''SELECT device_id , Date(from_unixtime(timestamp/1000)) as date , call_type, call_duration,
                        CASE 
                        WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 0 AND 6 THEN 'PART_1'
                        WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 6 AND 12 THEN 'PART_2'
                        WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 12 AND 18 THEN 'PART_3'
                        WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 18 AND 24 THEN 'PART_4'
                        END as part_of_the_day
                        from calls c
                        where call_type!=3'''
  #df_calls_duration = pd.read_sql(query_duration_calls,mydb)
  #df_calls_duration.to_csv("MySQL_output\Calls_duration_csv.csv")

  #Count AVG distinct users (trace) per type
  query_trace_calls='''select device_id, date, part_of_the_day, call_type, count(distinct trace) as dis_trace
                    from(
                    SELECT device_id , Date(from_unixtime(timestamp/1000)) as date , hour(from_unixtime(timestamp/1000)) AS hour , trace, call_type,
                    CASE 
                    WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 0 AND 6 THEN 'PART_1'
                    WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 6 AND 12 THEN 'PART_2'
                    WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 12 AND 18 THEN 'PART_3'
                    WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 18 AND 24 THEN 'PART_4'
                    END as part_of_the_day
                    from calls c) as sub1
                    group by device_id, date, part_of_the_day, call_type'''
  #df_calls_trace = pd.read_sql(query_trace_calls,mydb)
  #df_calls_trace.to_csv("MySQL_output\Calls_trace_csv.csv")

  #Messages
  query_messages='''SELECT device_id , Date(from_unixtime(timestamp/1000)) as date, message_type, trace,
                        CASE 
                        WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 0 AND 6 THEN 'PART_1'
                        WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 6 AND 12 THEN 'PART_2'
                        WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 12 AND 18 THEN 'PART_3'
                        WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 18 AND 24 THEN 'PART_4'
                        END as part_of_the_day
                        from messages m2'''
  #df_messages = pd.read_sql(query_messages,mydb)
  #df_messages.to_csv("MySQL_output\Messages_csv.csv")

  query_messages_num = '''select device_id ,message_type, date, count(message_type) as count_mes_type, part_of_the_day
                        from (
                        SELECT device_id , Date(from_unixtime(timestamp/1000)) as date , hour(from_unixtime(timestamp/1000)) AS hour , message_type,
                        CASE 
                        WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 0 AND 6 THEN 'PART_1'
                        WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 6 AND 12 THEN 'PART_2'
                        WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 12 AND 18 THEN 'PART_3'
                        WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 18 AND 24 THEN 'PART_4'
                        END as part_of_the_day
                        from messages m2) as sub
                        group by device_id, date, part_of_the_day, message_type'''
  #df_messages_num = pd.read_sql(query_messages_num,mydb)
  #df_messages_num.to_csv("MySQL_output\Messages_num_csv.csv")

  query_messages_trace = '''select device_id, date, part_of_the_day, count(distinct trace) as dis_trace
                          from(
                          SELECT device_id , Date(from_unixtime(timestamp/1000)) as date , hour(from_unixtime(timestamp/1000)) AS hour , trace,
                          CASE 
                          WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 0 AND 6 THEN 'PART_1'
                          WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 6 AND 12 THEN 'PART_2'
                          WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 12 AND 18 THEN 'PART_3'
                          WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 18 AND 24 THEN 'PART_4'
                          END as part_of_the_day
                          from messages m2 ) as sub1
                          group by device_id, date, part_of_the_day'''
  #df_messages_trace = pd.read_sql(query_messages_trace,mydb)
  #df_messages_trace.to_csv("MySQL_output\Messages_trace_csv.csv")

  #Screen
  # 1)AVG count screen on per part of the day
  query_screen_count = '''select device_id , Date(from_unixtime(timestamp/1000)) as date,
                            CASE 
                            WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 0 AND 6 THEN 'PART_1'
                            WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 6 AND 12 THEN 'PART_2'
                            WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 12 AND 18 THEN 'PART_3'
                            WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 18 AND 24 THEN 'PART_4'
                            END as part_of_the_day,
                            CASE 
                            WHEN screen_status = '1' THEN 1 
                            END as count_screen_on
                            from screen s2
                            where screen_status = '1'
                            '''
  #df_screen_count = pd.read_sql(query_screen_count,mydb)
  #df_screen_count.to_csv("MySQL_output\Screen_count_csv.csv")

  # 2)row data
  query_screen = '''select device_id , from_unixtime(timestamp/1000) as time, Date(from_unixtime(timestamp/1000)) as date, screen_status,
                            CASE 
                            WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 0 AND 6 THEN 'PART_1'
                            WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 6 AND 12 THEN 'PART_2'
                            WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 12 AND 18 THEN 'PART_3'
                            WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 18 AND 24 THEN 'PART_4'
                            END as part_of_the_day
                            from screen s2 
                            where screen_status = '1' or screen_status = '2';'''
  #df_screen = pd.read_sql(query_screen,mydb)
  #df_screen.to_csv("MySQL_output\Screen_csv.csv")

  #Wi-Fi
  query_wifi = '''select device_id ,Date(from_unixtime(timestamp/1000)) as date, count( DISTINCT ssid) as count_wifi,
                CASE 
                WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 0 AND 6 THEN 'PART_1'
                WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 6 AND 12 THEN 'PART_2'
                WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 12 AND 18 THEN 'PART_3'
                WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 18 AND 24 THEN 'PART_4'
                END as part_of_the_day
                from wifi 
                group by device_id, part_of_the_day, date'''
  #df_wifi = pd.read_sql(query_wifi,mydb)
  #df_wifi.to_csv("MySQL_output\Wifi_csv.csv")

  query_wifi_week = '''select device_id , count( DISTINCT ssid) as count_wifi
                from wifi 
                group by device_id
                '''
  #query_wifi_week = pd.read_sql(query_wifi_week,mydb)
  #query_wifi_week.to_csv("MySQL_output\Wifi_week_csv.csv")

  mydb.close() #close the connection

except Exception as e:
    mydb.close()
    print(str(e))


  """
  # Applications; category
  query_Applications_category='''SELECT device_id, Date(from_unixtime(timestamp/1000)) as date, application_name,
                              CASE 
                              when application_name in ('Launcher3','הורדות','אנשי קשר','MTP application',"'שימוש חכם בדיגיטל' ובקרת הורים",'Moto App Launcher','מקליט שיחות טלפון','דפדפן','הודעות','הקבצים שלי','‏מפעיל האפליקציות של Pixel','‏אנשי קשר','‏חייגן','מדיה ומכשירים','‏מקלדת LG','‏מערכת Android','מתקין החבילה','Settings','Microsoft Launcher','System UI','דף הבית של Huawei','חפש עדכוני מערכת','Google Play Store','העברת הודעות','Galaxy Store','Package installer','Samsung Internet','Google Play services','System Launcher','דף הבית של Samsung Experience','Samsung capture','Dual App','Firefox Focus',"'משגר היישומים' של המערכת",'EmergencyManagerService','Permission controller','מערכת Android','AlwaysOnDisplay','Aptoide','‏ממשק משתמש של המערכת','‏שירותי Google Play','Android Accessibility Suite','Gboard','LED Cover Service','Samsung DeX System UI','AOD (always-on display)','Contacts','Acrobat for Samsung','Always On Edge','com.samsung.android.biometrics.app.setting','Samsung Notes','Wallpapers','Microsoft SwiftKey Keyboard','Always On Display','Samsung Keyboard','Dialer','Phone','Android System','One UI Home','Call','שיחה','ממשק משתמש של המערכת','Huawei Share','Edge screen','drupe','טלפון','מקלדת Samsung','ClipboardUIService','ממשק המערכת','קבצים','דף הבית של One UI','מסך Edge','הגדרות') THEN "Phone"
                              when application_name in ('WhatsApp','Truecaller','Gmail','Messenger','מורפיקס','מורפיקס','Sheets','Chrome','Messages','Telegram','Firefox','Signal','‏WhatsApp','Duo','GBWhatsApp') THEN "Communication"
                              when application_name in ('Facebook','Instagram','Twitter','TikTok','פייסבוק','Lite','Me','‏טוויטר','Great Courses Plus') THEN "Social Media"
                              when application_name in ('Any.do','Drive','Docs','Calendar','יומן','לוח שנה','מחשבון','Gestures & Motions','Notion','‏בית','Dropbox','Raindrop','2 Battery','Adobe Acrobat','AI Search','Adobe Scan','Adobe Fill & Sign','CamScanner','Haifa','דוח אחד אוטומטי','‏הערות ב-Keep','כתוב על PDF','חמ”ל','דו"ח 1') THEN "Productive"
                              when application_name in ('Call Recorder','EasyOneHand','Google','‏Google‏','Clock','Calculator','Quickstep','Finder','Keep Notes','Weather','Office','Files by Google','Files','My Files','Excel','Translate','Accessibility','Account Access','Air command','AirBattery','Avast Mobile Security','Clean Master','AVG AntiVirus','Avast Cleanup','Authenticator','Bixby Routines','BlockerX','Followers & Unfollowers','מחפש','מזג אוויר','Word','רשמקול קליל','שעון','LastPass','Edge panels') THEN "Tools"
                              when application_name in ('Duolingo','YVC','TED','Emoji Blitz','אריאל','Udemy','Moodle') THEN "Education"
                              when application_name in ('Glance','Netflix','makoTV','9GAG','Eurovision','Meme Generator Free') THEN "Entertainment"
                              when application_name in ('Camera','Gallery','Photo Editor','Gallery Go','Photos','מצלמה','גלריה','צילום Samsung','‏מצלמה','תמונות') THEN "Photography"
                              when application_name in ('Maps','Waze','Google Go','חלוניות Edge','חנות Google Play','בקר הרשאות','Bird','bubble','Moovit','Gett','Yango','HopOn Rav-Pass','מפות') THEN "Maps and nevigation"
                              when application_name in ('YouTube','‏YouTube','YouTube Vanced','OnePlus Launcher','PL','סלקום tv','Shazam','Rumble','Video Player','Audible','BG Player','Music','iTube','AZ Screen Recorder','Spotify','YouTube Music') THEN "Music and Video editors"
                              when application_name in ('Shufersal','AliExpress','eBay','AddIt','Adika','Amazon Shopping','Avo','ASOS','SHEIN') THEN "Shooping"
                              when application_name in ('FlashScore','365Scores','Boost','Eurochamp','Fit','FitOn','Forza','Lose Belly Fat - Flat Stomach','ONE','Health','Samsung Health','כללית active') THEN "Sport"
                              when application_name in ('bit','1Money','Cal','Finance','אוצר החייל','בנק דיסקונט','בנק הפועלים','ישראכרט','כאל','PayBox','PAY','‏max‏') THEN "Finance"
                              when application_name in ('3 Tiles','Block Puzzle Jewel','Block Sudoku','Clash of Clans','Clash Royale','Space Gold','Games','Pokémon GO') THEN "Games"
                              when application_name in ('LinkedIn','Zoom','iPanel','‏WhatsApp Business') THEN "Buisness"
                              when application_name in ('ynet','הארץ','החדשות N12','כאן','כאן חינוכית') THEN "News"
                              when application_name in ('Booking.com','easy') THEN "Travel"
                              when application_name in ('AWARE','') THEN "Aware"
                              when application_name in ('ארומה ישראל','דומינוס פיצה','פיצה האט',"McDonald's Israel",'לגנדה','תן ביס','משלוחה','wolt') THEN "Food and Drinks"
                              when application_name in ('Tinder','Bumble','Hinge','OkCupid','JSwipe','Feeld','Heyoosh') THEN "The good life (dating)"
                              else application_name
                              END as app_category, 
                              CASE 
                              WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 0 AND 6 THEN 'PART_1'
                              WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 6 AND 12 THEN 'PART_2'
                              WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 12 AND 18 THEN 'PART_3'
                              WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 18 AND 24 THEN 'PART_4'
                              END as part_of_the_day
                              FROM applications_foreground'''
  #df_Applications_category = pd.read_sql(query_Applications_category,mydb)
  #df_Applications_category.to_csv("MySQL_output\Applications_category_csv.csv")

  # Applications; Whatsapp uses
  query_Applications_Whatsapp='''SELECT device_id, Date(from_unixtime(timestamp/1000)) as date, application_name, count(application_name) as counter,
                      CASE 
                      WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 0 AND 6 THEN 'PART_1'
                      WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 6 AND 12 THEN 'PART_2'
                      WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 12 AND 18 THEN 'PART_3'
                      WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 18 AND 24 THEN 'PART_4'
                      END as part_of_the_day
                      FROM applications_foreground
                      where application_name='WhatsApp' or application_name='‏WhatsApp' or application_name='WhatsApp Business' or application_name='GBWhatsApp'
                      group by device_id, date, part_of_the_day, application_name'''
  #df_Applications_Whatsapp = pd.read_sql(query_Applications_Whatsapp,mydb)
  #df_Applications_Whatsapp.to_csv("MySQL_output\Applications_Whatsapp_csv.csv")


  #Accelerometer
  query_Accelerometer = """SELECT device_id,Date(from_unixtime(timestamp/1000)) as date, double_values_0 as X_axis , double_values_1 as Y_axis, double_values_2 as Z_axis,
                          POW(pow(double_values_0,2)+pow(double_values_1,2)+pow(double_values_2,2), 0.5 ) as r_i,
                          CASE
                          WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 0 AND 6 THEN 'PART_1'
                          WHEN hour (from_unixtime(timestamp/1000)) BETWEEN 12 AND 18 THEN 'PART_3'
                          WHEN hour(from_unixtime(timestamp/1000)) BETWEEN 18 AND 24 THEN 'PART_4'
                          END as part_of_the_day
                          from accelerometer a;"""
  #df_Accelerometer = pd.read_sql(query_Accelerometer,mydb)
  #df_Accelerometer.to_csv("MySQL_output\Accelerometer_csv.csv")
  """
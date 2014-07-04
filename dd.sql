[{"fields": {"app_label": "admin", "name": "log entry", "model": "logentry"}, "model": "contenttypes.contenttype", "pk": 1}, {"fields": {"app_label": "auth", "name": "permission", "model": "permission"}, "model": "contenttypes.contenttype", "pk": 2}, {"fields": {"app_label": "auth", "name": "group", "model": "group"}, "model": "contenttypes.contenttype", "pk": 3}, {"fields": {"app_label": "auth", "name": "user", "model": "user"}, "model": "contenttypes.contenttype", "pk": 4}, {"fields": {"app_label": "contenttypes", "name": "content type", "model": "contenttype"}, "model": "contenttypes.contenttype", "pk": 5}, {"fields": {"app_label": "sessions", "name": "session", "model": "session"}, "model": "contenttypes.contenttype", "pk": 6}, {"fields": {"app_label": "restapi", "name": "prestataire", "model": "prestataire"}, "model": "contenttypes.contenttype", "pk": 7}, {"fields": {"app_label": "restapi", "name": "authentication", "model": "authentication"}, "model": "contenttypes.contenttype", "pk": 8}, {"fields": {"app_label": "restapi", "name": "type", "model": "type"}, "model": "contenttypes.contenttype", "pk": 9}, {"fields": {"app_label": "restapi", "name": "activite", "model": "activite"}, "model": "contenttypes.contenttype", "pk": 10}, {"fields": {"app_label": "restapi", "name": "prestation", "model": "prestation"}, "model": "contenttypes.contenttype", "pk": 11}, {"fields": {"app_label": "restapi", "name": "client", "model": "client"}, "model": "contenttypes.contenttype", "pk": 12}, {"fields": {"app_label": "restapi", "name": "ressource", "model": "ressource"}, "model": "contenttypes.contenttype", "pk": 13}, {"fields": {"app_label": "restapi", "name": "depend", "model": "depend"}, "model": "contenttypes.contenttype", "pk": 14}, {"fields": {"app_label": "restapi", "name": "event", "model": "event"}, "model": "contenttypes.contenttype", "pk": 15}, {"fields": {"app_label": "snippets", "name": "snippet", "model": "snippet"}, "model": "contenttypes.contenttype", "pk": 16}, {"fields": {"session_data": "YWM0ZWZhODFhY2Y3MjQ4NDk5NTRjNmFlNDE2YjA0OTJhMTQxNGUyYzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=", "expire_date": "2014-07-03T14:27:17.220Z"}, "model": "sessions.session", "pk": "4dq2fe3fy584b4biyzr34ufbqp407jg4"}, {"fields": {"session_data": "YWM0ZWZhODFhY2Y3MjQ4NDk5NTRjNmFlNDE2YjA0OTJhMTQxNGUyYzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=", "expire_date": "2014-07-03T14:31:15.025Z"}, "model": "sessions.session", "pk": "8u6dsxfwjguuj85lbwvq7g9mqzisehem"}, {"fields": {"use_condition": "En cas d'annulation, pr\u00e9venir par mail.\r\nMerci d'avance.", "name": "salon Exemple", "authentication": 1, "timezone": "Europe/Zurich"}, "model": "restapi.prestataire", "pk": 1}, {"fields": {"api_key": "1234-5467-8910"}, "model": "restapi.authentication", "pk": 1}, {"fields": {"prestataire": 1, "name": "Employe", "isSelectable": true, "isReservable": true}, "model": "restapi.type", "pk": 1}, {"fields": {"prestataire": 1, "name": "Succursales", "isSelectable": true, "isReservable": false}, "model": "restapi.type", "pk": 2}, {"fields": {"prestataire": 1, "name": "Si\u00e8ge", "isSelectable": false, "isReservable": true}, "model": "restapi.type", "pk": 3}, {"fields": {"types": [1, 2, 3], "name": "coupe homme", "prestataire": 1, "duration": 60}, "model": "restapi.activite", "pk": 1}, {"fields": {"types": [1, 2, 3], "name": "coupe femme", "prestataire": 1, "duration": 90}, "model": "restapi.activite", "pk": 2}, {"fields": {"prestataire": 1, "price": 50, "activityOrder": "1", "activitys": [1], "name": "Coupe homme", "duration": 0}, "model": "restapi.prestation", "pk": 1}, {"fields": {"prestataire": 1, "price": 100, "activityOrder": "1", "activitys": [2], "name": "Coupe femme", "duration": 0}, "model": "restapi.prestation", "pk": 2}, {"fields": {"content_type": 1, "name": "Can add log entry", "codename": "add_logentry"}, "model": "auth.permission", "pk": 1}, {"fields": {"content_type": 1, "name": "Can change log entry", "codename": "change_logentry"}, "model": "auth.permission", "pk": 2}, {"fields": {"content_type": 1, "name": "Can delete log entry", "codename": "delete_logentry"}, "model": "auth.permission", "pk": 3}, {"fields": {"content_type": 2, "name": "Can add permission", "codename": "add_permission"}, "model": "auth.permission", "pk": 4}, {"fields": {"content_type": 2, "name": "Can change permission", "codename": "change_permission"}, "model": "auth.permission", "pk": 5}, {"fields": {"content_type": 2, "name": "Can delete permission", "codename": "delete_permission"}, "model": "auth.permission", "pk": 6}, {"fields": {"content_type": 3, "name": "Can add group", "codename": "add_group"}, "model": "auth.permission", "pk": 7}, {"fields": {"content_type": 3, "name": "Can change group", "codename": "change_group"}, "model": "auth.permission", "pk": 8}, {"fields": {"content_type": 3, "name": "Can delete group", "codename": "delete_group"}, "model": "auth.permission", "pk": 9}, {"fields": {"content_type": 4, "name": "Can add user", "codename": "add_user"}, "model": "auth.permission", "pk": 10}, {"fields": {"content_type": 4, "name": "Can change user", "codename": "change_user"}, "model": "auth.permission", "pk": 11}, {"fields": {"content_type": 4, "name": "Can delete user", "codename": "delete_user"}, "model": "auth.permission", "pk": 12}, {"fields": {"content_type": 5, "name": "Can add content type", "codename": "add_contenttype"}, "model": "auth.permission", "pk": 13}, {"fields": {"content_type": 5, "name": "Can change content type", "codename": "change_contenttype"}, "model": "auth.permission", "pk": 14}, {"fields": {"content_type": 5, "name": "Can delete content type", "codename": "delete_contenttype"}, "model": "auth.permission", "pk": 15}, {"fields": {"content_type": 6, "name": "Can add session", "codename": "add_session"}, "model": "auth.permission", "pk": 16}, {"fields": {"content_type": 6, "name": "Can change session", "codename": "change_session"}, "model": "auth.permission", "pk": 17}, {"fields": {"content_type": 6, "name": "Can delete session", "codename": "delete_session"}, "model": "auth.permission", "pk": 18}, {"fields": {"content_type": 7, "name": "Can add prestataire", "codename": "add_prestataire"}, "model": "auth.permission", "pk": 19}, {"fields": {"content_type": 7, "name": "Can change prestataire", "codename": "change_prestataire"}, "model": "auth.permission", "pk": 20}, {"fields": {"content_type": 7, "name": "Can delete prestataire", "codename": "delete_prestataire"}, "model": "auth.permission", "pk": 21}, {"fields": {"content_type": 8, "name": "Can add authentication", "codename": "add_authentication"}, "model": "auth.permission", "pk": 22}, {"fields": {"content_type": 8, "name": "Can change authentication", "codename": "change_authentication"}, "model": "auth.permission", "pk": 23}, {"fields": {"content_type": 8, "name": "Can delete authentication", "codename": "delete_authentication"}, "model": "auth.permission", "pk": 24}, {"fields": {"content_type": 9, "name": "Can add type", "codename": "add_type"}, "model": "auth.permission", "pk": 25}, {"fields": {"content_type": 9, "name": "Can change type", "codename": "change_type"}, "model": "auth.permission", "pk": 26}, {"fields": {"content_type": 9, "name": "Can delete type", "codename": "delete_type"}, "model": "auth.permission", "pk": 27}, {"fields": {"content_type": 10, "name": "Can add activite", "codename": "add_activite"}, "model": "auth.permission", "pk": 28}, {"fields": {"content_type": 10, "name": "Can change activite", "codename": "change_activite"}, "model": "auth.permission", "pk": 29}, {"fields": {"content_type": 10, "name": "Can delete activite", "codename": "delete_activite"}, "model": "auth.permission", "pk": 30}, {"fields": {"content_type": 11, "name": "Can add prestation", "codename": "add_prestation"}, "model": "auth.permission", "pk": 31}, {"fields": {"content_type": 11, "name": "Can change prestation", "codename": "change_prestation"}, "model": "auth.permission", "pk": 32}, {"fields": {"content_type": 11, "name": "Can delete prestation", "codename": "delete_prestation"}, "model": "auth.permission", "pk": 33}, {"fields": {"content_type": 12, "name": "Can add client", "codename": "add_client"}, "model": "auth.permission", "pk": 34}, {"fields": {"content_type": 12, "name": "Can change client", "codename": "change_client"}, "model": "auth.permission", "pk": 35}, {"fields": {"content_type": 12, "name": "Can delete client", "codename": "delete_client"}, "model": "auth.permission", "pk": 36}, {"fields": {"content_type": 13, "name": "Can add ressource", "codename": "add_ressource"}, "model": "auth.permission", "pk": 37}, {"fields": {"content_type": 13, "name": "Can change ressource", "codename": "change_ressource"}, "model": "auth.permission", "pk": 38}, {"fields": {"content_type": 13, "name": "Can delete ressource", "codename": "delete_ressource"}, "model": "auth.permission", "pk": 39}, {"fields": {"content_type": 14, "name": "Can add depend", "codename": "add_depend"}, "model": "auth.permission", "pk": 40}, {"fields": {"content_type": 14, "name": "Can change depend", "codename": "change_depend"}, "model": "auth.permission", "pk": 41}, {"fields": {"content_type": 14, "name": "Can delete depend", "codename": "delete_depend"}, "model": "auth.permission", "pk": 42}, {"fields": {"content_type": 15, "name": "Can add event", "codename": "add_event"}, "model": "auth.permission", "pk": 43}, {"fields": {"content_type": 15, "name": "Can change event", "codename": "change_event"}, "model": "auth.permission", "pk": 44}, {"fields": {"content_type": 15, "name": "Can delete event", "codename": "delete_event"}, "model": "auth.permission", "pk": 45}, {"fields": {"content_type": 16, "name": "Can add snippet", "codename": "add_snippet"}, "model": "auth.permission", "pk": 46}, {"fields": {"content_type": 16, "name": "Can change snippet", "codename": "change_snippet"}, "model": "auth.permission", "pk": 47}, {"fields": {"content_type": 16, "name": "Can delete snippet", "codename": "delete_snippet"}, "model": "auth.permission", "pk": 48}, {"fields": {"date_joined": "2014-06-19T13:39:17.870Z", "last_name": "", "first_name": "", "username": "chassotce", "email": "", "is_active": true, "password": "pbkdf2_sha256$12000$D2MIywISWCDP$oMvgy/kuHpFE6Qw+jDHN52y0ycvYk1rpD9RN3O994wU=", "user_permissions": [], "groups": [], "last_login": "2014-06-19T14:31:15.020Z", "is_staff": true, "is_superuser": true}, "model": "auth.user", "pk": 1}, {"fields": {"date_joined": "2014-06-19T14:31:48Z", "last_name": "", "first_name": "", "username": "Jean", "email": "", "is_active": true, "password": "pbkdf2_sha256$12000$5K7fhmL6Tl8q$dq7TLlfldku8LWOIARBx2fhKzRigo15k5XP8ZYRHwy4=", "user_permissions": [], "groups": [], "last_login": "2014-06-19T14:31:48Z", "is_staff": true, "is_superuser": false}, "model": "auth.user", "pk": 2}, {"fields": {"date_joined": "2014-06-19T14:32:52Z", "last_name": "", "first_name": "", "username": "Marie", "email": "", "is_active": true, "password": "pbkdf2_sha256$12000$1994vlCcowQG$dPKWCS70eqg0/YfLyeLGOO+iewvsC2+GBTBim4rYiGY=", "user_permissions": [], "groups": [], "last_login": "2014-06-19T14:32:52Z", "is_staff": true, "is_superuser": false}, "model": "auth.user", "pk": 3}, {"fields": {"date_joined": "2014-06-19T14:33:22Z", "last_name": "", "first_name": "", "username": "Luc", "email": "", "is_active": true, "password": "pbkdf2_sha256$12000$w5Rw0lbz6vBK$eLboZB5BYbNOZ0OCUbDXBBBplngmXR/DFZtHHduBYH4=", "user_permissions": [], "groups": [], "last_login": "2014-06-19T14:33:22Z", "is_staff": true, "is_superuser": false}, "model": "auth.user", "pk": 4}, {"fields": {"date_joined": "2014-06-19T14:52:29Z", "last_name": "", "first_name": "", "username": "fribourg", "email": "", "is_active": true, "password": "pbkdf2_sha256$12000$kn1QxQiZRh48$/j3UE+R/mCTaRIt+mC0GNaahPY9Sf2KSwY0xGP3Iowk=", "user_permissions": [], "groups": [], "last_login": "2014-06-19T14:52:29Z", "is_staff": true, "is_superuser": false}, "model": "auth.user", "pk": 5}, {"fields": {"date_joined": "2014-06-19T14:53:03Z", "last_name": "", "first_name": "", "username": "marly", "email": "", "is_active": true, "password": "pbkdf2_sha256$12000$rzC5X3lOlRUj$YbUjGrjgx4bqryG1nPhK03cHvzcSo5Ozn/dUcxJ2zL0=", "user_permissions": [], "groups": [], "last_login": "2014-06-19T14:53:03Z", "is_staff": true, "is_superuser": false}, "model": "auth.user", "pk": 6}, {"fields": {"date_joined": "2014-06-19T14:53:59Z", "last_name": "", "first_name": "", "username": "siege1", "email": "", "is_active": true, "password": "pbkdf2_sha256$12000$cJxXJXLbZ1ZN$HJnoFNikQ89rSFXd3x4jfbhqW8J0nS4pHd53W1H87Hk=", "user_permissions": [], "groups": [], "last_login": "2014-06-19T14:53:59Z", "is_staff": true, "is_superuser": false}, "model": "auth.user", "pk": 7}, {"fields": {"date_joined": "2014-06-20T07:08:28Z", "last_name": "", "first_name": "", "username": "siege2", "email": "", "is_active": true, "password": "pbkdf2_sha256$12000$FmgIlcjvFmXu$NeHX5rb1ewruJF6mfVhswf8vHZ00Eo+Tv2BoEBwVKCY=", "user_permissions": [], "groups": [], "last_login": "2014-06-20T07:08:28Z", "is_staff": true, "is_superuser": false}, "model": "auth.user", "pk": 8}, {"fields": {"date_joined": "2014-06-20T07:09:33Z", "last_name": "", "first_name": "", "username": "siege3", "email": "", "is_active": true, "password": "pbkdf2_sha256$12000$CgEQQILQtFK5$kew+bdxYSXu1p2mVt2ZmFqzRtKh0qGDyVVqYmQrfvPM=", "user_permissions": [], "groups": [], "last_login": "2014-06-20T07:09:33Z", "is_staff": true, "is_superuser": false}, "model": "auth.user", "pk": 9}, {"fields": {"email": "jean@exemple.com", "type": 1, "prestataire": 1, "ressources": [4], "activitys": [1], "user": 2, "name": "Jean", "isAdmin": false}, "model": "restapi.ressource", "pk": 1}, {"fields": {"email": "marie@exemple.com", "type": 1, "prestataire": 1, "ressources": [5], "activitys": [1, 2], "user": 3, "name": "Marie", "isAdmin": false}, "model": "restapi.ressource", "pk": 2}, {"fields": {"email": "luc@exemple.com", "type": 1, "prestataire": 1, "ressources": [5], "activitys": [1, 2], "user": 4, "name": "Luc", "isAdmin": false}, "model": "restapi.ressource", "pk": 3}, {"fields": {"email": "fribourg@fri.com", "type": 2, "prestataire": 1, "ressources": [1, 8], "activitys": [1, 2], "user": 5, "name": "fribourg", "isAdmin": false}, "model": "restapi.ressource", "pk": 4}, {"fields": {"email": "marly@exemple.com", "type": 2, "prestataire": 1, "ressources": [2, 3, 6, 7], "activitys": [1, 2], "user": 6, "name": "marly", "isAdmin": false}, "model": "restapi.ressource", "pk": 5}, {"fields": {"email": "siege1@exemple.com", "type": 3, "prestataire": 1, "ressources": [5], "activitys": [1, 2], "user": 7, "name": "siege1", "isAdmin": false}, "model": "restapi.ressource", "pk": 6}, {"fields": {"email": "siege2@exemple.com", "type": 3, "prestataire": 1, "ressources": [5], "activitys": [1, 2], "user": 8, "name": "siege2", "isAdmin": false}, "model": "restapi.ressource", "pk": 7}, {"fields": {"email": "siege3@exemple.com", "type": 3, "prestataire": 1, "ressources": [4], "activitys": [1, 2], "user": 9, "name": "siege3", "isAdmin": false}, "model": "restapi.ressource", "pk": 8}, {"fields": {"object_id": "2", "object_repr": "Jean", "content_type": 4, "user": 1, "change_message": "", "action_time": "2014-06-19T14:31:48.929Z", "action_flag": 1}, "model": "admin.logentry", "pk": 1}, {"fields": {"object_id": "3", "object_repr": "Marie", "content_type": 4, "user": 1, "change_message": "", "action_time": "2014-06-19T14:32:52.237Z", "action_flag": 1}, "model": "admin.logentry", "pk": 2}, {"fields": {"object_id": "4", "object_repr": "Luc", "content_type": 4, "user": 1, "change_message": "", "action_time": "2014-06-19T14:33:22.653Z", "action_flag": 1}, "model": "admin.logentry", "pk": 3}, {"fields": {"object_id": "4", "object_repr": "Luc", "content_type": 4, "user": 1, "change_message": "Changed is_staff.", "action_time": "2014-06-19T14:33:37.793Z", "action_flag": 2}, "model": "admin.logentry", "pk": 4}, {"fields": {"object_id": "2", "object_repr": "Jean", "content_type": 4, "user": 1, "change_message": "Changed is_staff.", "action_time": "2014-06-19T14:33:48.701Z", "action_flag": 2}, "model": "admin.logentry", "pk": 5}, {"fields": {"object_id": "3", "object_repr": "Marie", "content_type": 4, "user": 1, "change_message": "Changed is_staff.", "action_time": "2014-06-19T14:33:56.063Z", "action_flag": 2}, "model": "admin.logentry", "pk": 6}, {"fields": {"object_id": "5", "object_repr": "fribourg", "content_type": 4, "user": 1, "change_message": "", "action_time": "2014-06-19T14:52:30.025Z", "action_flag": 1}, "model": "admin.logentry", "pk": 7}, {"fields": {"object_id": "6", "object_repr": "marly", "content_type": 4, "user": 1, "change_message": "", "action_time": "2014-06-19T14:53:03.320Z", "action_flag": 1}, "model": "admin.logentry", "pk": 8}, {"fields": {"object_id": "7", "object_repr": "siege1", "content_type": 4, "user": 1, "change_message": "", "action_time": "2014-06-19T14:54:00.068Z", "action_flag": 1}, "model": "admin.logentry", "pk": 9}, {"fields": {"object_id": "8", "object_repr": "siege2", "content_type": 4, "user": 1, "change_message": "", "action_time": "2014-06-20T07:08:28.616Z", "action_flag": 1}, "model": "admin.logentry", "pk": 10}, {"fields": {"object_id": "9", "object_repr": "siege3", "content_type": 4, "user": 1, "change_message": "", "action_time": "2014-06-20T07:09:33.361Z", "action_flag": 1}, "model": "admin.logentry", "pk": 11}, {"fields": {"object_id": "7", "object_repr": "siege1", "content_type": 4, "user": 1, "change_message": "Changed is_staff. Changed ressources for ressource \"siege1\".", "action_time": "2014-06-20T07:10:04.588Z", "action_flag": 2}, "model": "admin.logentry", "pk": 12}, {"fields": {"object_id": "5", "object_repr": "fribourg", "content_type": 4, "user": 1, "change_message": "Changed is_staff.", "action_time": "2014-06-20T07:10:17.269Z", "action_flag": 2}, "model": "admin.logentry", "pk": 13}, {"fields": {"object_id": "6", "object_repr": "marly", "content_type": 4, "user": 1, "change_message": "Changed is_staff.", "action_time": "2014-06-20T07:10:24.744Z", "action_flag": 2}, "model": "admin.logentry", "pk": 14}, {"fields": {"object_id": "8", "object_repr": "siege2", "content_type": 4, "user": 1, "change_message": "Changed is_staff.", "action_time": "2014-06-20T07:10:35.326Z", "action_flag": 2}, "model": "admin.logentry", "pk": 15}, {"fields": {"object_id": "9", "object_repr": "siege3", "content_type": 4, "user": 1, "change_message": "Changed is_staff.", "action_time": "2014-06-20T07:10:47.719Z", "action_flag": 2}, "model": "admin.logentry", "pk": 16}, {"fields": {"object_id": "2", "object_repr": "Jean", "content_type": 4, "user": 1, "change_message": "Changed ressources for ressource \"Jean\".", "action_time": "2014-06-20T07:11:11.794Z", "action_flag": 2}, "model": "admin.logentry", "pk": 17}, {"fields": {"object_id": "7", "object_repr": "siege1", "content_type": 4, "user": 1, "change_message": "No fields changed.", "action_time": "2014-06-20T07:11:20.241Z", "action_flag": 2}, "model": "admin.logentry", "pk": 18}, {"fields": {"object_id": "8", "object_repr": "siege2", "content_type": 4, "user": 1, "change_message": "Changed ressources for ressource \"siege2\".", "action_time": "2014-06-20T07:11:27.909Z", "action_flag": 2}, "model": "admin.logentry", "pk": 19}, {"fields": {"object_id": "9", "object_repr": "siege3", "content_type": 4, "user": 1, "change_message": "No fields changed.", "action_time": "2014-06-20T07:11:42.057Z", "action_flag": 2}, "model": "admin.logentry", "pk": 20}, {"fields": {"object_id": "4", "object_repr": "Luc", "content_type": 4, "user": 1, "change_message": "Changed ressources for ressource \"Luc\".", "action_time": "2014-06-20T07:11:53.464Z", "action_flag": 2}, "model": "admin.logentry", "pk": 21}, {"fields": {"object_id": "3", "object_repr": "Marie", "content_type": 4, "user": 1, "change_message": "Changed ressources for ressource \"Marie\".", "action_time": "2014-06-20T07:12:03.988Z", "action_flag": 2}, "model": "admin.logentry", "pk": 22}]
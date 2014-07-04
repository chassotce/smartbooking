BEGIN TRANSACTION;
CREATE TABLE "auth_group" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(80) NOT NULL UNIQUE
);
CREATE TABLE "auth_group_permissions" (
    "id" integer NOT NULL PRIMARY KEY,
    "group_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"),
    UNIQUE ("group_id", "permission_id")
);
CREATE TABLE "auth_permission" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(50) NOT NULL,
    "content_type_id" integer NOT NULL,
    "codename" varchar(100) NOT NULL,
    UNIQUE ("content_type_id", "codename")
);
INSERT INTO "auth_permission" VALUES(1,'Can add log entry',1,'add_logentry');
INSERT INTO "auth_permission" VALUES(2,'Can change log entry',1,'change_logentry');
INSERT INTO "auth_permission" VALUES(3,'Can delete log entry',1,'delete_logentry');
INSERT INTO "auth_permission" VALUES(4,'Can add permission',2,'add_permission');
INSERT INTO "auth_permission" VALUES(5,'Can change permission',2,'change_permission');
INSERT INTO "auth_permission" VALUES(6,'Can delete permission',2,'delete_permission');
INSERT INTO "auth_permission" VALUES(7,'Can add group',3,'add_group');
INSERT INTO "auth_permission" VALUES(8,'Can change group',3,'change_group');
INSERT INTO "auth_permission" VALUES(9,'Can delete group',3,'delete_group');
INSERT INTO "auth_permission" VALUES(10,'Can add user',4,'add_user');
INSERT INTO "auth_permission" VALUES(11,'Can change user',4,'change_user');
INSERT INTO "auth_permission" VALUES(12,'Can delete user',4,'delete_user');
INSERT INTO "auth_permission" VALUES(13,'Can add content type',5,'add_contenttype');
INSERT INTO "auth_permission" VALUES(14,'Can change content type',5,'change_contenttype');
INSERT INTO "auth_permission" VALUES(15,'Can delete content type',5,'delete_contenttype');
INSERT INTO "auth_permission" VALUES(16,'Can add session',6,'add_session');
INSERT INTO "auth_permission" VALUES(17,'Can change session',6,'change_session');
INSERT INTO "auth_permission" VALUES(18,'Can delete session',6,'delete_session');
INSERT INTO "auth_permission" VALUES(19,'Can add prestataire',7,'add_prestataire');
INSERT INTO "auth_permission" VALUES(20,'Can change prestataire',7,'change_prestataire');
INSERT INTO "auth_permission" VALUES(21,'Can delete prestataire',7,'delete_prestataire');
INSERT INTO "auth_permission" VALUES(22,'Can add authentication',8,'add_authentication');
INSERT INTO "auth_permission" VALUES(23,'Can change authentication',8,'change_authentication');
INSERT INTO "auth_permission" VALUES(24,'Can delete authentication',8,'delete_authentication');
INSERT INTO "auth_permission" VALUES(25,'Can add type',9,'add_type');
INSERT INTO "auth_permission" VALUES(26,'Can change type',9,'change_type');
INSERT INTO "auth_permission" VALUES(27,'Can delete type',9,'delete_type');
INSERT INTO "auth_permission" VALUES(28,'Can add activite',10,'add_activite');
INSERT INTO "auth_permission" VALUES(29,'Can change activite',10,'change_activite');
INSERT INTO "auth_permission" VALUES(30,'Can delete activite',10,'delete_activite');
INSERT INTO "auth_permission" VALUES(31,'Can add prestation',11,'add_prestation');
INSERT INTO "auth_permission" VALUES(32,'Can change prestation',11,'change_prestation');
INSERT INTO "auth_permission" VALUES(33,'Can delete prestation',11,'delete_prestation');
INSERT INTO "auth_permission" VALUES(34,'Can add client',12,'add_client');
INSERT INTO "auth_permission" VALUES(35,'Can change client',12,'change_client');
INSERT INTO "auth_permission" VALUES(36,'Can delete client',12,'delete_client');
INSERT INTO "auth_permission" VALUES(37,'Can add ressource',13,'add_ressource');
INSERT INTO "auth_permission" VALUES(38,'Can change ressource',13,'change_ressource');
INSERT INTO "auth_permission" VALUES(39,'Can delete ressource',13,'delete_ressource');
INSERT INTO "auth_permission" VALUES(40,'Can add depend',14,'add_depend');
INSERT INTO "auth_permission" VALUES(41,'Can change depend',14,'change_depend');
INSERT INTO "auth_permission" VALUES(42,'Can delete depend',14,'delete_depend');
INSERT INTO "auth_permission" VALUES(43,'Can add event',15,'add_event');
INSERT INTO "auth_permission" VALUES(44,'Can change event',15,'change_event');
INSERT INTO "auth_permission" VALUES(45,'Can delete event',15,'delete_event');
INSERT INTO "auth_permission" VALUES(46,'Can add snippet',16,'add_snippet');
INSERT INTO "auth_permission" VALUES(47,'Can change snippet',16,'change_snippet');
INSERT INTO "auth_permission" VALUES(48,'Can delete snippet',16,'delete_snippet');
CREATE TABLE "auth_user" (
    "id" integer NOT NULL PRIMARY KEY,
    "password" varchar(128) NOT NULL,
    "last_login" datetime NOT NULL,
    "is_superuser" bool NOT NULL,
    "username" varchar(30) NOT NULL UNIQUE,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL,
    "email" varchar(75) NOT NULL,
    "is_staff" bool NOT NULL,
    "is_active" bool NOT NULL,
    "date_joined" datetime NOT NULL
);
INSERT INTO "auth_user" VALUES(1,'pbkdf2_sha256$12000$D2MIywISWCDP$oMvgy/kuHpFE6Qw+jDHN52y0ycvYk1rpD9RN3O994wU=','2014-06-19 14:31:15.020149',1,'chassotce','','','',1,1,'2014-06-19 13:39:17.870228');
INSERT INTO "auth_user" VALUES(2,'pbkdf2_sha256$12000$5K7fhmL6Tl8q$dq7TLlfldku8LWOIARBx2fhKzRigo15k5XP8ZYRHwy4=','2014-06-19 14:31:48',0,'Jean','','','',1,1,'2014-06-19 14:31:48');
INSERT INTO "auth_user" VALUES(3,'pbkdf2_sha256$12000$1994vlCcowQG$dPKWCS70eqg0/YfLyeLGOO+iewvsC2+GBTBim4rYiGY=','2014-06-19 14:32:52',0,'Marie','','','',1,1,'2014-06-19 14:32:52');
INSERT INTO "auth_user" VALUES(4,'pbkdf2_sha256$12000$w5Rw0lbz6vBK$eLboZB5BYbNOZ0OCUbDXBBBplngmXR/DFZtHHduBYH4=','2014-06-19 14:33:22',0,'Luc','','','',1,1,'2014-06-19 14:33:22');
INSERT INTO "auth_user" VALUES(5,'pbkdf2_sha256$12000$kn1QxQiZRh48$/j3UE+R/mCTaRIt+mC0GNaahPY9Sf2KSwY0xGP3Iowk=','2014-06-19 14:52:29',0,'fribourg','','','',1,1,'2014-06-19 14:52:29');
INSERT INTO "auth_user" VALUES(6,'pbkdf2_sha256$12000$rzC5X3lOlRUj$YbUjGrjgx4bqryG1nPhK03cHvzcSo5Ozn/dUcxJ2zL0=','2014-06-19 14:53:03',0,'marly','','','',1,1,'2014-06-19 14:53:03');
INSERT INTO "auth_user" VALUES(7,'pbkdf2_sha256$12000$cJxXJXLbZ1ZN$HJnoFNikQ89rSFXd3x4jfbhqW8J0nS4pHd53W1H87Hk=','2014-06-19 14:53:59',0,'siege1','','','',1,1,'2014-06-19 14:53:59');
INSERT INTO "auth_user" VALUES(8,'pbkdf2_sha256$12000$FmgIlcjvFmXu$NeHX5rb1ewruJF6mfVhswf8vHZ00Eo+Tv2BoEBwVKCY=','2014-06-20 07:08:28',0,'siege2','','','',1,1,'2014-06-20 07:08:28');
INSERT INTO "auth_user" VALUES(9,'pbkdf2_sha256$12000$CgEQQILQtFK5$kew+bdxYSXu1p2mVt2ZmFqzRtKh0qGDyVVqYmQrfvPM=','2014-06-20 07:09:33',0,'siege3','','','',1,1,'2014-06-20 07:09:33');
CREATE TABLE "auth_user_groups" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "group_id" integer NOT NULL REFERENCES "auth_group" ("id"),
    UNIQUE ("user_id", "group_id")
);
CREATE TABLE "auth_user_user_permissions" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"),
    UNIQUE ("user_id", "permission_id")
);
CREATE TABLE "django_admin_log" (
    "id" integer NOT NULL PRIMARY KEY,
    "action_time" datetime NOT NULL,
    "user_id" integer NOT NULL,
    "content_type_id" integer,
    "object_id" text,
    "object_repr" varchar(200) NOT NULL,
    "action_flag" smallint unsigned NOT NULL,
    "change_message" text NOT NULL
);
INSERT INTO "django_admin_log" VALUES(1,'2014-06-19 14:31:48.929624',1,4,'2','Jean',1,'');
INSERT INTO "django_admin_log" VALUES(2,'2014-06-19 14:32:52.237502',1,4,'3','Marie',1,'');
INSERT INTO "django_admin_log" VALUES(3,'2014-06-19 14:33:22.653941',1,4,'4','Luc',1,'');
INSERT INTO "django_admin_log" VALUES(4,'2014-06-19 14:33:37.793636',1,4,'4','Luc',2,'Changed is_staff.');
INSERT INTO "django_admin_log" VALUES(5,'2014-06-19 14:33:48.701327',1,4,'2','Jean',2,'Changed is_staff.');
INSERT INTO "django_admin_log" VALUES(6,'2014-06-19 14:33:56.063292',1,4,'3','Marie',2,'Changed is_staff.');
INSERT INTO "django_admin_log" VALUES(7,'2014-06-19 14:52:30.025527',1,4,'5','fribourg',1,'');
INSERT INTO "django_admin_log" VALUES(8,'2014-06-19 14:53:03.320898',1,4,'6','marly',1,'');
INSERT INTO "django_admin_log" VALUES(9,'2014-06-19 14:54:00.068594',1,4,'7','siege1',1,'');
INSERT INTO "django_admin_log" VALUES(10,'2014-06-20 07:08:28.616605',1,4,'8','siege2',1,'');
INSERT INTO "django_admin_log" VALUES(11,'2014-06-20 07:09:33.361007',1,4,'9','siege3',1,'');
INSERT INTO "django_admin_log" VALUES(12,'2014-06-20 07:10:04.588374',1,4,'7','siege1',2,'Changed is_staff. Changed ressources for ressource "siege1".');
INSERT INTO "django_admin_log" VALUES(13,'2014-06-20 07:10:17.269487',1,4,'5','fribourg',2,'Changed is_staff.');
INSERT INTO "django_admin_log" VALUES(14,'2014-06-20 07:10:24.744840',1,4,'6','marly',2,'Changed is_staff.');
INSERT INTO "django_admin_log" VALUES(15,'2014-06-20 07:10:35.326559',1,4,'8','siege2',2,'Changed is_staff.');
INSERT INTO "django_admin_log" VALUES(16,'2014-06-20 07:10:47.719365',1,4,'9','siege3',2,'Changed is_staff.');
INSERT INTO "django_admin_log" VALUES(17,'2014-06-20 07:11:11.794481',1,4,'2','Jean',2,'Changed ressources for ressource "Jean".');
INSERT INTO "django_admin_log" VALUES(18,'2014-06-20 07:11:20.241264',1,4,'7','siege1',2,'No fields changed.');
INSERT INTO "django_admin_log" VALUES(19,'2014-06-20 07:11:27.909623',1,4,'8','siege2',2,'Changed ressources for ressource "siege2".');
INSERT INTO "django_admin_log" VALUES(20,'2014-06-20 07:11:42.057604',1,4,'9','siege3',2,'No fields changed.');
INSERT INTO "django_admin_log" VALUES(21,'2014-06-20 07:11:53.464081',1,4,'4','Luc',2,'Changed ressources for ressource "Luc".');
INSERT INTO "django_admin_log" VALUES(22,'2014-06-20 07:12:03.988652',1,4,'3','Marie',2,'Changed ressources for ressource "Marie".');
CREATE TABLE "django_content_type" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(100) NOT NULL,
    "app_label" varchar(100) NOT NULL,
    "model" varchar(100) NOT NULL,
    UNIQUE ("app_label", "model")
);
INSERT INTO "django_content_type" VALUES(1,'log entry','admin','logentry');
INSERT INTO "django_content_type" VALUES(2,'permission','auth','permission');
INSERT INTO "django_content_type" VALUES(3,'group','auth','group');
INSERT INTO "django_content_type" VALUES(4,'user','auth','user');
INSERT INTO "django_content_type" VALUES(5,'content type','contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES(6,'session','sessions','session');
INSERT INTO "django_content_type" VALUES(7,'prestataire','restapi','prestataire');
INSERT INTO "django_content_type" VALUES(8,'authentication','restapi','authentication');
INSERT INTO "django_content_type" VALUES(9,'type','restapi','type');
INSERT INTO "django_content_type" VALUES(10,'activite','restapi','activite');
INSERT INTO "django_content_type" VALUES(11,'prestation','restapi','prestation');
INSERT INTO "django_content_type" VALUES(12,'client','restapi','client');
INSERT INTO "django_content_type" VALUES(13,'ressource','restapi','ressource');
INSERT INTO "django_content_type" VALUES(14,'depend','restapi','depend');
INSERT INTO "django_content_type" VALUES(15,'event','restapi','event');
INSERT INTO "django_content_type" VALUES(16,'snippet','snippets','snippet');
CREATE TABLE "django_session" (
    "session_key" varchar(40) NOT NULL PRIMARY KEY,
    "session_data" text NOT NULL,
    "expire_date" datetime NOT NULL
);
INSERT INTO "django_session" VALUES('4dq2fe3fy584b4biyzr34ufbqp407jg4','YWM0ZWZhODFhY2Y3MjQ4NDk5NTRjNmFlNDE2YjA0OTJhMTQxNGUyYzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-07-03 14:27:17.220197');
INSERT INTO "django_session" VALUES('8u6dsxfwjguuj85lbwvq7g9mqzisehem','YWM0ZWZhODFhY2Y3MjQ4NDk5NTRjNmFlNDE2YjA0OTJhMTQxNGUyYzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-07-03 14:31:15.025483');
CREATE TABLE "restapi_activite" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(20) NOT NULL,
    "duration" integer unsigned NOT NULL,
    "prestataire_id" integer NOT NULL REFERENCES "restapi_prestataire" ("id")
);
INSERT INTO "restapi_activite" VALUES(1,'coupe homme',60,1);
INSERT INTO "restapi_activite" VALUES(2,'coupe femme',90,1);
CREATE TABLE "restapi_activite_types" (
    "id" integer NOT NULL PRIMARY KEY,
    "activite_id" integer NOT NULL,
    "type_id" integer NOT NULL REFERENCES "restapi_type" ("id"),
    UNIQUE ("activite_id", "type_id")
);
INSERT INTO "restapi_activite_types" VALUES(1,1,1);
INSERT INTO "restapi_activite_types" VALUES(2,1,2);
INSERT INTO "restapi_activite_types" VALUES(3,1,3);
INSERT INTO "restapi_activite_types" VALUES(4,2,1);
INSERT INTO "restapi_activite_types" VALUES(5,2,2);
INSERT INTO "restapi_activite_types" VALUES(6,2,3);
CREATE TABLE "restapi_authentication" (
    "id" integer NOT NULL PRIMARY KEY,
    "api_key" varchar(20) NOT NULL UNIQUE
);
INSERT INTO "restapi_authentication" VALUES(1,'1234-5467-8910');
CREATE TABLE "restapi_client" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(255) NOT NULL,
    "mail" varchar(75) NOT NULL,
    "adress" varchar(255) NOT NULL,
    "phone" varchar(255) NOT NULL,
    "prestataire_id" integer NOT NULL REFERENCES "restapi_prestataire" ("id")
);
CREATE TABLE "restapi_depend" (
    "id" integer NOT NULL PRIMARY KEY,
    "ressource_from_id" integer NOT NULL REFERENCES "restapi_ressource" ("id"),
    "ressource_to_id" integer NOT NULL REFERENCES "restapi_ressource" ("id")
);
CREATE TABLE "restapi_event" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(255) NOT NULL,
    "type" varchar(255) NOT NULL,
    "state" varchar(255) NOT NULL,
    "start" datetime NOT NULL,
    "end" datetime NOT NULL,
    "rule" varchar(255),
    "client_id" integer REFERENCES "restapi_client" ("id"),
    "prestation_id" integer REFERENCES "restapi_prestation" ("id"),
    "activity_id" integer REFERENCES "restapi_activite" ("id"),
    "prestataire_id" integer NOT NULL REFERENCES "restapi_prestataire" ("id")
);
CREATE TABLE "restapi_event_ressources" (
    "id" integer NOT NULL PRIMARY KEY,
    "event_id" integer NOT NULL,
    "ressource_id" integer NOT NULL REFERENCES "restapi_ressource" ("id"),
    UNIQUE ("event_id", "ressource_id")
);
CREATE TABLE "restapi_prestataire" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(20) NOT NULL,
    "timezone" varchar(250) NOT NULL,
    "use_condition" varchar(1024) NOT NULL,
    "authentication_id" integer NOT NULL
);
INSERT INTO "restapi_prestataire" VALUES(1,'salon Exemple','Europe/Zurich','En cas d''annulation, prévenir par mail.
Merci d''avance.',1);
CREATE TABLE "restapi_prestation" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(20) NOT NULL,
    "duration" integer unsigned NOT NULL,
    "price" integer unsigned NOT NULL,
    "activityOrder" varchar(1024) NOT NULL,
    "prestataire_id" integer NOT NULL REFERENCES "restapi_prestataire" ("id")
);
INSERT INTO "restapi_prestation" VALUES(1,'Coupe homme',0,50,'1',1);
INSERT INTO "restapi_prestation" VALUES(2,'Coupe femme',0,100,'1',1);
CREATE TABLE "restapi_prestation_activitys" (
    "id" integer NOT NULL PRIMARY KEY,
    "prestation_id" integer NOT NULL,
    "activite_id" integer NOT NULL REFERENCES "restapi_activite" ("id"),
    UNIQUE ("prestation_id", "activite_id")
);
INSERT INTO "restapi_prestation_activitys" VALUES(1,1,1);
INSERT INTO "restapi_prestation_activitys" VALUES(2,2,2);
CREATE TABLE "restapi_ressource" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id"),
    "name" varchar(255) NOT NULL,
    "email" varchar(75) NOT NULL,
    "isAdmin" bool NOT NULL,
    "type_id" integer NOT NULL REFERENCES "restapi_type" ("id"),
    "prestataire_id" integer NOT NULL REFERENCES "restapi_prestataire" ("id")
);
INSERT INTO "restapi_ressource" VALUES(1,2,'Jean','jean@exemple.com',0,1,1);
INSERT INTO "restapi_ressource" VALUES(2,3,'Marie','marie@exemple.com',0,1,1);
INSERT INTO "restapi_ressource" VALUES(3,4,'Luc','luc@exemple.com',0,1,1);
INSERT INTO "restapi_ressource" VALUES(4,5,'fribourg','fribourg@fri.com',0,2,1);
INSERT INTO "restapi_ressource" VALUES(5,6,'marly','marly@exemple.com',0,2,1);
INSERT INTO "restapi_ressource" VALUES(6,7,'siege1','siege1@exemple.com',0,3,1);
INSERT INTO "restapi_ressource" VALUES(7,8,'siege2','siege2@exemple.com',0,3,1);
INSERT INTO "restapi_ressource" VALUES(8,9,'siege3','siege3@exemple.com',0,3,1);
CREATE TABLE "restapi_ressource_activitys" (
    "id" integer NOT NULL PRIMARY KEY,
    "ressource_id" integer NOT NULL,
    "activite_id" integer NOT NULL REFERENCES "restapi_activite" ("id"),
    UNIQUE ("ressource_id", "activite_id")
);
INSERT INTO "restapi_ressource_activitys" VALUES(6,4,1);
INSERT INTO "restapi_ressource_activitys" VALUES(7,4,2);
INSERT INTO "restapi_ressource_activitys" VALUES(8,5,1);
INSERT INTO "restapi_ressource_activitys" VALUES(9,5,2);
INSERT INTO "restapi_ressource_activitys" VALUES(14,8,1);
INSERT INTO "restapi_ressource_activitys" VALUES(15,8,2);
INSERT INTO "restapi_ressource_activitys" VALUES(16,6,1);
INSERT INTO "restapi_ressource_activitys" VALUES(17,6,2);
INSERT INTO "restapi_ressource_activitys" VALUES(18,1,1);
INSERT INTO "restapi_ressource_activitys" VALUES(19,7,1);
INSERT INTO "restapi_ressource_activitys" VALUES(20,7,2);
INSERT INTO "restapi_ressource_activitys" VALUES(21,3,1);
INSERT INTO "restapi_ressource_activitys" VALUES(22,3,2);
INSERT INTO "restapi_ressource_activitys" VALUES(23,2,1);
INSERT INTO "restapi_ressource_activitys" VALUES(24,2,2);
CREATE TABLE "restapi_ressource_ressources" (
    "id" integer NOT NULL PRIMARY KEY,
    "from_ressource_id" integer NOT NULL,
    "to_ressource_id" integer NOT NULL,
    UNIQUE ("from_ressource_id", "to_ressource_id")
);
INSERT INTO "restapi_ressource_ressources" VALUES(3,8,4);
INSERT INTO "restapi_ressource_ressources" VALUES(4,4,8);
INSERT INTO "restapi_ressource_ressources" VALUES(5,6,5);
INSERT INTO "restapi_ressource_ressources" VALUES(6,5,6);
INSERT INTO "restapi_ressource_ressources" VALUES(7,1,4);
INSERT INTO "restapi_ressource_ressources" VALUES(8,4,1);
INSERT INTO "restapi_ressource_ressources" VALUES(9,7,5);
INSERT INTO "restapi_ressource_ressources" VALUES(10,5,7);
INSERT INTO "restapi_ressource_ressources" VALUES(11,3,5);
INSERT INTO "restapi_ressource_ressources" VALUES(12,5,3);
INSERT INTO "restapi_ressource_ressources" VALUES(13,2,5);
INSERT INTO "restapi_ressource_ressources" VALUES(14,5,2);
CREATE TABLE "restapi_type" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(20) NOT NULL,
    "isSelectable" bool NOT NULL,
    "isReservable" bool NOT NULL,
    "prestataire_id" integer NOT NULL REFERENCES "restapi_prestataire" ("id")
);
INSERT INTO "restapi_type" VALUES(1,'Employe',1,1,1);
INSERT INTO "restapi_type" VALUES(2,'Succursales',1,0,1);
INSERT INTO "restapi_type" VALUES(3,'Siège',0,1,1);
CREATE TABLE "snippets_snippet" (
    "id" integer NOT NULL PRIMARY KEY,
    "created" datetime NOT NULL,
    "title" varchar(100) NOT NULL,
    "code" text NOT NULL,
    "linenos" bool NOT NULL,
    "language" varchar(100) NOT NULL,
    "style" varchar(100) NOT NULL,
    "owner_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "highlighted" text NOT NULL
);
CREATE INDEX "django_admin_log_6340c63c" ON "django_admin_log" ("user_id");
CREATE INDEX "django_admin_log_37ef4eb4" ON "django_admin_log" ("content_type_id");
CREATE INDEX "auth_permission_37ef4eb4" ON "auth_permission" ("content_type_id");
CREATE INDEX "auth_group_permissions_5f412f9a" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_83d7f98b" ON "auth_group_permissions" ("permission_id");
CREATE INDEX "auth_user_groups_6340c63c" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_5f412f9a" ON "auth_user_groups" ("group_id");
CREATE INDEX "auth_user_user_permissions_6340c63c" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_83d7f98b" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "django_session_b7b81f0c" ON "django_session" ("expire_date");
CREATE INDEX "restapi_prestataire_552eca41" ON "restapi_prestataire" ("authentication_id");
CREATE INDEX "restapi_type_70ae38ea" ON "restapi_type" ("prestataire_id");
CREATE INDEX "restapi_activite_types_b9ad2a94" ON "restapi_activite_types" ("activite_id");
CREATE INDEX "restapi_activite_types_403d8ff3" ON "restapi_activite_types" ("type_id");
CREATE INDEX "restapi_activite_70ae38ea" ON "restapi_activite" ("prestataire_id");
CREATE INDEX "restapi_prestation_activitys_42d741a7" ON "restapi_prestation_activitys" ("prestation_id");
CREATE INDEX "restapi_prestation_activitys_b9ad2a94" ON "restapi_prestation_activitys" ("activite_id");
CREATE INDEX "restapi_prestation_70ae38ea" ON "restapi_prestation" ("prestataire_id");
CREATE INDEX "restapi_client_70ae38ea" ON "restapi_client" ("prestataire_id");
CREATE INDEX "restapi_ressource_ressources_82e79f96" ON "restapi_ressource_ressources" ("from_ressource_id");
CREATE INDEX "restapi_ressource_ressources_97ebb778" ON "restapi_ressource_ressources" ("to_ressource_id");
CREATE INDEX "restapi_ressource_activitys_09a29d01" ON "restapi_ressource_activitys" ("ressource_id");
CREATE INDEX "restapi_ressource_activitys_b9ad2a94" ON "restapi_ressource_activitys" ("activite_id");
CREATE INDEX "restapi_ressource_403d8ff3" ON "restapi_ressource" ("type_id");
CREATE INDEX "restapi_ressource_70ae38ea" ON "restapi_ressource" ("prestataire_id");
CREATE INDEX "restapi_depend_8cb9efee" ON "restapi_depend" ("ressource_from_id");
CREATE INDEX "restapi_depend_f7d5e59b" ON "restapi_depend" ("ressource_to_id");
CREATE INDEX "restapi_event_ressources_a41e20fe" ON "restapi_event_ressources" ("event_id");
CREATE INDEX "restapi_event_ressources_09a29d01" ON "restapi_event_ressources" ("ressource_id");
CREATE INDEX "restapi_event_4fea5d6a" ON "restapi_event" ("client_id");
CREATE INDEX "restapi_event_42d741a7" ON "restapi_event" ("prestation_id");
CREATE INDEX "restapi_event_8005e431" ON "restapi_event" ("activity_id");
CREATE INDEX "restapi_event_70ae38ea" ON "restapi_event" ("prestataire_id");
CREATE INDEX "snippets_snippet_cb902d83" ON "snippets_snippet" ("owner_id");
COMMIT;

---
title:  "Thunderbird AutoConfig"
tags:
  - thunderbird
  - tutorial
---

{% include toc %}
[MCD,_Mission_Control_Desktop_AKA_AutoConfig](https://developer.mozilla.org/en-US/docs/MCD,_Mission_Control_Desktop_AKA_AutoConfig){:target="_blank"}

# Thunderbird Cli

## Enable AutoConfig
add those lines at the end of this file:
```shell
nano /etc/thunderbird/pref/thunderbird.js
```
```shell
...
pref("general.config.obscure_value", 0); // for MCD .cfg files
pref("general.config.filename", "thunderbird.cfg"); // for MCD .cfg files
```

## TB AutoConfig
```shell
nano /usr/lib/thunderbird/thunderbird.cfg
```
```shell
//put everything in a try/catch
try {

// 1) env variables
if(getenv("USER") != "") {
  // *NIX settings
  var env_user = getenv("USER");
  var env_home = getenv("HOME");
} else {
  // Windows settings
  var env_user = getenv("USERNAME");
  var env_home = getenv("HOMEPATH");
}
var env_mozdebug= getenv("MOZILLA_DEBUG");
// var env_user = prompt("indiquez votre login", titi);

// lock general preferences
//LDAP address book
lockPref("ldap_2.prefs_migrated", true);
lockPref("ldap_2.servers.LDAPINT.auth.savePassword", true);
lockPref("ldap_2.servers.LDAPINT.description", "LDAPCONTACTS");
lockPref("ldap_2.servers.LDAPINT.filename", "abook-1.mab");
lockPref("ldap_2.servers.LDAPINT.uri", "ldap://ldapcontacts:389/dc=contacts");
lockPref("ldap_2.servers.history.filename", "history.mab");
lockPref("ldap_2.servers.history.replication.lastChangeNumber", 0);
lockPref("ldap_2.servers.pab.filename", "abook.mab");
lockPref("ldap_2.servers.pab.replication.lastChangeNumber", 0);

lockPref("ldap_2.autoComplete.directoryServer", "ldap_2.servers.LDAPINT");
lockPref("ldap_2.autoComplete.useDirectory", true);
lockPref("pref.ldap.disable_button.edit_directories", false);

// Caldav calendar "user"
lockPref("calendar.registry.cal-id-user.imip.identity.key", "");
lockPref("calendar.registry.cal-id-user.name", env_user);
lockPref("calendar.registry.cal-id-user.readOnly", false);
lockPref("calendar.registry.cal-id-user.type", "caldav");
lockPref("calendar.registry.cal-id-user.uri",
"https://caldavsrv:9191/caldav.php/" + env_user + "/calendar/");
defaultPref("calendar.registry.cal-id-user.disabled", false);

// Caldav shared calendar "holidays"
lockPref("calendar.registry.cal-id-holidays.imip.identity.key", "");
lockPref("calendar.registry.cal-id-holidays.name", "holidays");
lockPref("calendar.registry.cal-id-holidays.readOnly", false);
lockPref("calendar.registry.cal-id-holidays.type", "caldav");
lockPref("calendar.registry.cal-id-holidays.uri",
"https://caldavsrv:9191/caldav.php/holidays/calendar/");
defaultPref("calendar.registry.cal-id-holidays.disabled", false);

// disable chat
lockPref("messenger.startup.action", 0);
// disable statup page
lockPref("mailnews.start_page.enabled", false);
// set mail alerts at 5s
pref("alerts.totalOpenTime", 5000);
// Enable sig
pref("mail.identity.id1.sig_file", "/home/" + env_user  + "/signature.html");
pref("mail.identity.id1.attach_signature", true);

// Disable data submission
lockPref("datareporting.policy.dataSubmissionEnabled", false);


// Close the try, and call the catch()
} catch(e) {
  displayError("lockedPref", e);
}

```

# Mail Settings

## Enable AutoConfig
On your domain webserver:
```shell
mkdir -p /var/www/siddou.tk/.well-known/autoconfig/mail
```

```shell
nano /var/www/siddou.tk/.well-known/autoconfig/mail/config-v1.1.xml
```
```shell
<clientConfig version="1.0">
    <emailProvider id="siddou.tk">
          <domain>siddou.tk</domain>
          <displayName>Siddou Mail server</displayName>
          <displayShortName>Sidd</displayShortName>
          <incomingServer type="imap">
                <hostname>imap.siddou.tk</hostname>
                <port>993</port>
                <socketType>SSL</socketType>
                <username>%EMAILLOCALPART%</username>
                <authentication>plain</authentication>
          </incomingServer>
          <outgoingServer type="smtp">
                <hostname>smtp.siddou.tk</hostname>
                <port>587</port>
                <socketType>STARTTLS</socketType>
                <authentication>plain</authentication>
                <username>%EMAILLOCALPART%</username>
          </outgoingServer>
    </emailProvider>
</clientConfig>
```

Now when adding a new mail account in TB, the correct settings will be automatically filled.


{% include comments.html %}
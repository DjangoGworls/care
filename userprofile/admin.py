from userprofile.models import UserProfile, NotificationInterval
#from accounts.models import Account
from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['user']}),
    (None, {'fields': ['displayname']}),
    (None, {'fields': ['groupAccounts']}),
    (None, {'fields': ['showTableView']}),
    (None, {'fields': ['historyEmailInterval']}),
  ]
  
  list_display = ('user', 'displayname', 'showTableView', 'historyEmailInterval')


class NotificationIntervalAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['name']}),
    (None, {'fields': ['days']}),
  ]
  
  list_display = ('name', 'days',)
    
#class AccountAdmin(admin.ModelAdmin):
    #fieldsets = [
        #(None, {'fields': ['name']}),
        #(None, {'fields': ['owner']}),
        #(None, {'fields': ['friends']}),
    #]
    #list_display = ('name', 'owner',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(NotificationInterval, NotificationIntervalAdmin)

#admin.site.register(Account, AccountAdmin)

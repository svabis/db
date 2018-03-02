# -*- coding: utf-8 -*-

# Klienta modelis
from clients.models import Klienti

# Abonementi
from subscriptions.models import Abonementi

import datetime
from datetime import timedelta

import pytz
tz = pytz.timezone('EET')

#==============================================================
class ActiveSubscription(object):
    exists = False # ir abonements, kuru var lietot TAGAD ?
    active = [] # TAGAD lietojamais abonements, ja ir...
    today = datetime.datetime.now().replace(tzinfo=tz)

# CONSTRUCTOR
    def __init__(self, cli):
       # 1. atlasa visus ended = False, frozen = True --> EXIT
        subscriptions = Abonementi.objects.filter( client = cli, ended = False, frozen = True )
        if subscriptions.count() > 0:
            return
       # 2. atlasa visus ended = False, active = True, secība sākot no senāk pirktā
        subscriptions = Abonementi.objects.filter( client = cli, ended = False, active = True ).order_by('purchase_date')
       # 3. pēc kārtas pārbauda vai der tagad un tūlīt, ja jā --> active, exist=True
        for s in subscriptions:
            temp = self.test( s )
            if temp == True:
                self.active = s
                self.exists = True
                return
       # 4. atlasa visus ended = False, active = False, secība sākot no senāk pirktā
        subscriptions = Abonementi.objects.filter( client = cli, ended = False, active = False ).order_by('purchase_date')
       # 5. pēc kārtas pārbauda vai der tagad un tūlīt, ja jā --> active, exist=True
        for s in subscriptions:
            temp = self.test( s )
            if temp == True:
                self.active = s
                self.exists = True
                return
       # 6. exist = False, active = [] (jeb self.x neko nemaina)


# Testa funkcija
    def test(self, obj):
       # 1. nosaka datetime un laiku
        today = datetime.datetime.now()
        time = datetime.time()
       # 2. nosaka weekday nummuru
        day = today.weekday()

       # 3. nav ne laika limiti, ne reizes un nav ended --> return True
        if obj.subscr.time_limit == False and obj.subscr.times == False:
            return True

       # 4. nav laika limits, ja ir reižu skaita reizes, ja ir --> return True
        if obj.subscr.time_limit == False:
            if obj.subscr.times == True:
                if obj.times_count > 0:
                    return True

        test_times = False # lai skripts veic pārbaudi uz reizēm...

       # 5. laika limits ir, pārbauda darbadienu laiku limitus, ja ir --> uz reižu pārbaudi
        if day >= 0 and day <= 4:
            if obj.subscr.time_limit_type.weekday1 == True:
                if obj.subscr.time_limit_type.weekday1_start_time < time < obj.subscr.weekday1_end_time:
                    test_times = True
            if obj.subscr.time_limit_type.weekday2 == True:
                if obj.subscr.time_limit_type.weekday2_start_time < time < obj.subscr.weekday2_end_time:
                    test_times = True

       # 6. laika limits ir, pārbauda brīvdienu laika limitu, ja ir --> uz reižu pārbaudi
        if day == 5 or day == 6:
            if obj.subscr.time_limit_type.weekend == True:
                if obj.subscr.time_limit_type.weekend_start_time < time < obj.subscr.weekend_end_time:
                    test_times = True

       # 7. "reižu pārbaude" --> ja i reižu un reizes ir --> return True, ja nav reižu --> return True
        if test_times == True: # pārbaudam vai nav reižu abonements...
            if obj.subscr.times == True: # ir, tad skaitam vai ir reizes...
                if obj.times_count > 0:
                    return True
            else: # nav reižu abonements (bet jau iepriekš noteikts ka iekļaujās laika limitos)
                return True

       # 7. Kaut kāda hrena dēļ neder nekur :D
#        return False


#==============================================================
class SubscriptionEnd(object):

# CONSTRUCTOR
    def __init__(self, cli):
       # 1. nosaka datetime un laiku
        today = datetime.datetime.now().replace(tzinfo=tz)
       # 2. Atlasa visus kuri nav beigušies
        subscriptions = Abonementi.objects.filter( client = cli, ended = False) #, frozen = True )
       # 3. iet cauri visiem...
        for s in subscriptions:
          # ja aktivēts, tad "best_before"
           if s.active:
               if s.best_before < today:
                   s.ended = True
                   s.save()
          # neaktivētam "activate_before"
           else:
               if s.activate_before < today:
                   s.ended = True
                   s.save()

"""
abonementu endotājs:

??? vai var endot IESALDĒTU ???

1. atlasa visus ended = False, frozen = False un ņem pēc kārtas -->

1.1. activate == False un activate_before < dateime.datetime.now() --> KILL
1.2. best_before < dateime.datetime.now() --> KILL
1.3. times == True --> times_count == 0 --> KILL

"""


#==============================================================
class SubscriptionUse(object):

# CONSTRUCTOR
    def __init__(self, abon):
        today = datetime.datetime.now()
       # Atrod izmantojamo Abonemetu:
        subscription = Abonementi.objects.get( id = abon )

       # Aktivē, ja nav aktivēts
        if subscription.active == False:
            subscription.active = True
            subscription.activation_date = today
            subscription.best_before = today + timedelta(days = 30)
            subscription.save()

       # Testē reizes
        if subscription.subscr.times:
            subscription.times_count = subscription.times_count -1

            if subscription.times_count == 0:
                subscription.ended = True

            subscription.save()

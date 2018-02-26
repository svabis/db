# -*- coding: utf-8 -*-

# Klienta modelis
from clients.models import Klienti

# Abonementi
from subscriptions.models import Abonementi

import datetime

#==============================================================
class ActiveSubscription(object):
    exists = False # ir abonements, kuru var lietot TAGAD ?
    active = [] # TAGAD lietojamais abonements, ja ir...

# CONSTRUCTOR
    def __init__(self, cli):
       # 1.
        subscriptions = Abonementi.objects.filter( client = cli, ended = False, frozen = True )
        if subscriptions.count() > 0:
            return
       # 2.
        subscriptions = Abonementi.objects.filter( client = cli, ended = False, active = True ).order_by('purchase_date')
       # 3.
        for s in subscriptions:
            temp = self.test( s )
            if temp == True:
                self.active = s
                self.exists = True
                return
       # 4.
        subscriptions = Abonementi.objects.filter( client = cli, ended = False, active = False ).order_by('purchase_date')
       # 5.
        for s in subscriptions:
            temp = self.test( s )
            if temp == True:
                self.active = s
                self.exists = True
                return
       # 6.

# Testa funkcija
    def test(self, obj):
       # 1.
        today = datetime.datetime.now()
        time = datetime.time()
       # 2.
        day = today.weekday()

       # 3.
        if obj.subscr.time_limit == False and obj.subscr.times == False:
            return True

       # 4. laika limits = nav
        if obj.subscr.time_limit == False:
            if obj.subscr.times == True:
                if obj.subscr.times_count > 0:
                    return True

        test_times = False # lai skripts veic pārbaudi uz reizēm...

       # 5. laika limits = ir
        if day >= 0 and day <= 4:
            if obj.subscr.time_limit_type.weekday1 == True:
                if obj.subscr.time_limit_type.weekday1_start_time < time < obj.subscr.weekday1_end_time:
                    test_times = True
            if obj.subscr.time_limit_type.weekday2 == True:
                if obj.subscr.time_limit_type.weekday2_start_time < time < obj.subscr.weekday2_end_time:
                    test_times = True

       # 6. laika limits = ir
        if day == 5 or day == 6:
            if obj.subscr.time_limit_type.weekend == True:
                if obj.subscr.time_limit_type.weekend_start_time < time < obj.subscr.weekend_end_time:
                    test_times = True

       # 4-ā veidīgs.
        if test_times == True: # pārbaudam vai nav reižu abonements...
            if obj.subscr.times == True: # ir, tad skaitam vai ir reizes...
                if obj.subscr.times_count > 0:
                    return True
            else: # nav reižu abonements (bet jau iepriekš noteikts ka iekļaujās laika limitos)
                return True

       # 7.
        return False


"""
KONSTRUKTORS
1. atlas visus ended = False, frozen = True --> EXIT

2. atlasa visus ended = False, active = True, secība sākot no senāk pirktā
3. pēc kārtas pārbauda vai der tagad un tūlīt, ja jā --> active, exist=True <-- funkcija test
4. atlasa visus ended = False, active = False, secība sākot no senāk pirktā
5. pēc kārtas pārbauda vai der tagad un tūlīt, ja jā --> active, exist=True <-- funkcija test
6. exist = False, active = [] (jeb self.x neko nemaina)

TEST
1. nosaka datetime.datetime.now()
2. nosaka ^ weekday nummuru

3. nav ne laika limiti, ne reizes un nav ended --> return True

4. ja abonements.subscr.time_limit == False -->
  --> abonements.subscr.times == True --> abonements.subscr.times_count > 0 tad --> return True

5. ja weekday_nr 0...4 (darbadiena) -->
  --> abonements.subscr.time_limit_type.weekday1 == True --> datetime.datetime.now() ietilpst iekš range --> 4-ā veidīgs
  --> abonements.subscr.time_limit_type.weekday2 == True --> datetime.datetime.now() ietilpst iekš range --> 4-ā veidīgs

6. ja weekday_nr == 5 or weekday_nr == 6 -->
  --> abonements.subscr.time_limit_type.weekend == True --> datetime.datetime.now() ietilpst iekš range --> 4-ā veidīgs

7. return False

"""

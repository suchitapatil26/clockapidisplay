
from django.http import HttpResponse,Http404

import datetime
import clockapi.talkingclock as tc
from django.http import JsonResponse

# Create your views here.
def currentDateTime(request,timedisplay):


        clk = tc.TalkingClock()
        textform=clk.humanFriendlyText(timedisplay)
        return JsonResponse({'clockText':textform})




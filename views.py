from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# import csrf fro CSRF protection
from django.views.decorators.csrf import csrf_exempt
# import df_library 
from library.df_response_lib import *
# import json to get json request
import json

# define home function 
def home(request):
    return HttpResponse('Hello, World!')

@csrf_exempt
def webhook(request):
	# build request object
	req = json.loads(request.body)

	#get action from json
	action = req.get('queryResult').get('action')

	if action == 'get_test':

		reply = {'fulfillmentText': 'This is Django test response from webhook.'}

	# response for suggestion chips
	if action == 'get_suggestion_chips':

		# set fulfillment text
		fulfillmentText = 'Suggestion chips Response from webhook'

		aog = actions_on_google_response()
		aog_sr = aog.simple_response([
			[fulfillmentText, fulfillmentText, False]
		])

		# create suggestion chips
		aog_sc = aog.suggestion_chips(["suggestion1", "suggestion2"])

		ff_response = fulfillment_response()
		ff_text = ff_response.fulfillment_text(fulfillmentText)
		ff_messages = ff_response.fulfillment_messages([aog_sr, aog_sc])

		reply = ff_response.main_response(ff_text, ff_messages)

	# response for basic card
	if action == 'get_basiccard':

		fulfillmentText = 'Basic card Response from webhook'

		aog = actions_on_google_response()
		aog_sr = aog.simple_response([
			[fulfillmentText, fulfillmentText, False]
		])

		basic_card = aog.basic_card("Title", "Subtitle", "This is formatted text", image=["https://www.pragnakalp.com/wp-content/uploads/2018/12/logo-1024.png", "this is accessibility text"])

		ff_response = fulfillment_response()
		ff_text = ff_response.fulfillment_text(fulfillmentText)
		ff_messages = ff_response.fulfillment_messages([aog_sr, basic_card])

		reply = ff_response.main_response(ff_text, ff_messages)

	# response for link out suggestion
	if action == 'get_link':

		fulfillmentText = 'link out suggestion Response from webhook'

		aog = actions_on_google_response()
		aog_sr = aog.simple_response([
			[fulfillmentText, fulfillmentText, False]
		])

		link_out_suggestion = aog.link_out_suggestion("Pragnakalp Techlabs", "https://pragnakalp.com")

		ff_response = fulfillment_response()
		ff_text = ff_response.fulfillment_text(fulfillmentText)
		ff_messages = ff_response.fulfillment_messages([aog_sr, link_out_suggestion])

		reply = ff_response.main_response(ff_text, ff_messages)

	# response for list
	if action == 'get_list':

		fulfillmentText = 'List Response from webhook'

		aog = actions_on_google_response()
		aog_sr = aog.simple_response([
			[fulfillmentText, fulfillmentText, False]
		])

		list_arr = [
			["Title1", "Description1", ["item1", "item2"], ["https://www.pragnakalp.com/wp-content/uploads/2018/12/logo-1024.png", "Pragnakalp Techlabs"]],["Title2", "Description2", ["item1", "item2"], ["https://www.pragnakalp.com/wp-content/uploads/2018/12/logo-1024.png", "Pragnakalp Techlabs"]]
		]

		list_select = aog.list_select("List Title", list_arr)

		ff_response = fulfillment_response()
		ff_text = ff_response.fulfillment_text(fulfillmentText)
		ff_messages = ff_response.fulfillment_messages([aog_sr, list_select])

		reply = ff_response.main_response(ff_text, ff_messages)

		return JsonResponse(reply, safe=False)

	# response for carousel card
	if action == 'get_carousel':

		fulfillmentText = 'Carousel card response from webhook'

		aog = actions_on_google_response()
		aog_sr = aog.simple_response([
			[fulfillmentText, fulfillmentText, False]
		])

		carousel_arr = [
			["Title1", "Description1", ["item1", "item2"], ["https://www.pragnakalp.com/wp-content/uploads/2018/12/logo-1024.png", "Pragnakalp Techlabs"]],["Title2", "Description2", ["item1", "item2"], ["https://www.pragnakalp.com/wp-content/uploads/2018/12/logo-1024.png", "Pragnakalp Techlabs"]]
		]

		carousel_select = aog.carousel_select(carousel_arr)

		ff_response = fulfillment_response()
		ff_text = ff_response.fulfillment_text(fulfillmentText)
		ff_messages = ff_response.fulfillment_messages([aog_sr, carousel_select])

		reply = ff_response.main_response(ff_text, ff_messages)

		return JsonResponse(reply, safe=False)

	# response for Browse carousel card
	if action == 'get_browse_carousel':

		fulfillmentText = 'Browse carousel card response from webhook'

		aog = actions_on_google_response()
		aog_sr = aog.simple_response([
			[fulfillmentText, fulfillmentText, False]
		])

		browse_carousel_arr = [
			["Title1", ["https://www.pragnakalp.com/wp-content/uploads/2018/12/logo-1024.png", "title1"], "https://www.pragnakalp.com/blog"], ["Pragnakalp Techlabs", ["https://www.pragnakalp.com/wp-content/uploads/2018/12/logo-1024.png", "Pragnakalp Techlabs"], "https://www.pragnakalp.com/blog"]
		]

		carousel_browse = aog.carousel_browse(browse_carousel_arr)

		ff_response = fulfillment_response()
		ff_text = ff_response.fulfillment_text(fulfillmentText)
		ff_messages = ff_response.fulfillment_messages([aog_sr, carousel_browse])

		reply = ff_response.main_response(ff_text, ff_messages)

	# return created response
	return JsonResponse(reply, safe=False)
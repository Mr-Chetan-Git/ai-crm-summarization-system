# import torch


# DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
# SEED = 42


# # Shared model config
# D_MODEL = 64
# NUM_HEADS = 4
# NUM_LAYERS = 2
# D_FF = 128
# MAX_LEN = 32


# # Sentiment task config
# SENTIMENT_EPOCHS = 40
# SENTIMENT_BATCH_SIZE = 4
# SENTIMENT_LR = 1e-3
# SENTIMENT_LABELS = {"negative": 0, "positive": 1}
# SENTIMENT_ID_TO_LABEL = {0: "negative", 1: "positive"}

# SENTIMENT_DATA = [
#     ("i love this movie", "positive"),
#     ("this film is amazing", "positive"),
#     ("what a fantastic story", "positive"),
#     ("i enjoyed every minute", "positive"),
#     ("the acting was great", "positive"),
#     ("i hate this movie", "negative"),
#     ("this film is terrible", "negative"),
#     ("what a boring story", "negative"),
#     ("i disliked every minute", "negative"),
#     ("the acting was awful", "negative"),
# ]


# # Summarization task config
# SUMMARIZATION_EPOCHS = 80

# SUMMARIZATION_BATCH_SIZE = 2
# SUMMARIZATION_LR = 1e-3
# MAX_SRC_LEN = 24
# MAX_TGT_LEN = 40



# SUMMARIZATION_DATA = [

#     (
#         "12may-no response 11may-no response 9may-no response 8may-no response 7may-no response 5may- driving will call later 24 apr he can;t for few batches no time 6 apr he will join the next batch right now he is busy with job switch and interviews 4-Apr given invite for first class 2 apr went through the sylllabus and fees he asked to share all the course and demo video on his whatsapp 2 apr not answering,",
#         "Customer initially reviewed syllabus, fees, and requested demo materials on WhatsApp. Repeated follow-ups later received no response due to job switch and busy schedule."
#     ),

#     (
#         "13-May Naveen called 7032940309 and informed to pay 20k and block it and will give 3 months payment plan 6 may-interested. call w naveen tmrw from 1-2 30-Apr She said on 7032940309 will call in the evening. 30-Apr Naveen in touch on whatsapp on these numbers 7032940309 28-Apr busy 27-Apr no response 20 apr discounts given she will think and tell by this saturday 19 apr joining 17-Apr no response 15 apr send syllabus 15-Apr Send syllabus on whatsapp 7032940309, send invit for Saturday event 15-Apr call in 30 mts 11 apr not answering 8 apr she said can't give number mail is fine 2 apr sent mail 1 apr number not on whatsapp i tried calling back she didn't answer i texted her through imessage 1 apr went through the syllabus she asked about the courses and fees then after listening fees she said i have to think about this then i told her about the trainer market and all",
#         "Customer showed interest after syllabus and fee discussions with flexible payment options. Follow-up communication continued through WhatsApp, calls, and event invitations despite delayed responses."
#     ),

#     (
#         "7may-he said naveen called and i told him im not interested 6may-no answer 30 apr i am not liking the curriculum so don't contact 28-Apr number not reachable 20-Apr Naveen given Demo video 19 apr voice mail 15-Apr Naveen to send Syllabus now he is intrested he is not intersted in AWS and no discount given 15 apr texted me inconsitently while you reply talk to me 3- Naveen had a syllabus walkthrough and long discussion . He is on touch on whatsapp and does not want discount 2 apr he received the call i said hello am i speakimg to aditya he disconnected without saying anything and now call is been forwarded to voice mail 2 apr i am in a hurry i have some work some you can whatsapp me or call me later",
#         "Customer initially engaged through syllabus walkthroughs and demo discussions with selective course interest. Later expressed dissatisfaction with the curriculum and declined further enrollment communication."
#     ),

#     (
#         "10 apr he said fees is only problem right now i said i will check internally he said everthing is fantastic only fees is the problem , shared demo video 7 apr texted me yes i have gone through the syllabus all the topics are very important 2-Apr send him intermediate sylalbus 1 apr i said him that that course is for senior people with atleast 10 years of exp but we also have intermediate course and system design i don't know what to speak so i said i will share the syllabus senior team will comtact you 1 apr call around 1:30 1 apr not answering",
#         "Customer appreciated the syllabus and course quality during discussions. Pricing concerns remained the primary obstacle preventing immediate enrollment confirmation."
#     ),

#     (
#         "2 apr i don't how it has registered i don;t know but honestly i am not looking for any courses right now ya i hopw you understand 2 apr called at 3 forwadred to voicemail 2 apr i am in ameeting can you call me at 3 pm today",
#         "Customer clarified no current interest in pursuing courses or enrollment opportunities. Meetings and voicemail responses limited further communication and follow-up discussions."
#     ),

#     (
#         "13may-no response 12may-no response 11may-no response 9may-no response 7may-call on weekend 6may-call in second half 29 call at 5 5-30 27 apr call declined 25 apr call declined 23-Apr no response 20-Apr given the demo video 18 apr joining 10-Apr He will call in one hour 9 apr course is focused on software architect his aim is to be ai architect so he is confused naveen can call him between 4-5 he is free pnly at that time 3-apr Naveen had a syllabus walkthrough 2 apr he texted syllabus is very good but price vise he has some concerns 2 apr no response 1 april called around 2 in meeting call in evening 1 apr he said he has 8 years of exp then he asked you are callingfrom ? then ii said i about walking through the syllabus he said right now its not a good time acutually you can share the syllabus then we can have a call around 2",
#         "Customer showed interest in AI architecture learning and attended syllabus discussions. Pricing concerns, career confusion, and repeated unavailability delayed enrollment decisions and follow-ups."
#     ),

#     (
#         "13may-busy 12may-busy 11may-busy 9may-busy 8may-busy 7may-busy 5may busy 30 apr call later 29 apr not answering 27 apr not answering 25 apr no response 24 apr currently busy , no response 22-Apr no response 21-Apr Given 1.99L , Naveen to send Syllabus again 18 apr in hospital right now talk to you later 15 apr not answering 10 apr i am driving right now just send a hi so i will look through the syllabus and get back to you 1 apr he said call in 5 mins i again called now he is not answering 1 apr before we start anything i first want the cirrculum to be sent then we can have a call in the evning because i want to know what you are covering i said i will walk you theough the syllabus tthrough the call it won't take a lot of time of yours he sais ya but office hours i can't pay attention so you send me first then lets have a call",
#         "Customer remained consistently busy and unavailable during follow-up communication attempts. Syllabus sharing and pricing discussions continued, but enrollment confirmation stayed pending afterward."
#     ),

#     (
#         "2-Apr had a discusion intersted more in AI she is from .net background. Naveen said will call and give discount 2 apr went through the syllabus and shared fees details",
#         "Customer from a .NET background showed strong interest in AI-focused learning opportunities. Syllabus, fee details, and discount discussions were completed during follow-up communication."
#     ),

#     (
#         "5may no response 4may syllabus is sent, didnt have time for syllabus walkthrough. he'll reply on whatsapp if hes interested 2may not answering 24 apr no response 16 apr not answering 14 apr not answering 11 apr no response , not answering 10 apr no response 9 apr currently busy 8 apr no response 6 apr not asnwering 4 apr not asnwering 2 apr no response 2 apr not answering",
#         "Customer received syllabus materials but remained mostly unavailable for discussions afterward. Repeated follow-up attempts resulted in no response, busy schedules, and unanswered calls."
#     ),

#     (
#         "2 apr call cannot be connected because third party cannot forward the call at the moment",
#         "Customer communication could not proceed because calls failed to connect properly. Technical call forwarding issues prevented successful follow-up discussions."
#     ),

#     (
#         "2 apr ya i have registered for the system deisgn thing but due to my health i can't proceed thsi further 2 apr not answering 1 apr he is an old lead from nov batch he is not answering",
#         "Customer registered earlier but could not continue because of health-related issues. Follow-up communication remained inactive with repeated unanswered calls afterward."
#     ),

#     (
#         "5may no response 4 may no response 2 may busy 25 apr no response 16 apr no response 14 apr not answering 11 apr not asnwering , call declined 10 apr no response 9 apr i am in office very busy call me after 6 ( i tried after 6 he didn't answer) it was not updated on the sheet because the sheet was showing unable to upload 9 apr not asnwering 8 apr not answering 6 apr not asnwering 4 apr not asnwering 2 apr not answering",
#         "Customer remained mostly unavailable because of office commitments and busy schedules. Repeated follow-up attempts resulted in unanswered calls, declined communication, and no responses afterward."
#     ),

#     (
#         "4 apr voice mail 2 apr voice mail",
#         "Customer communication attempts consistently redirected to voicemail responses. Meaningful follow-up discussions could not be established afterward."
#     ),

#     (
#         "8 apr texted kindly leave msg on whatsapp 6 apr not asnwering 4 apr anyday if you want call later 2 apr not asnwering",
#         "Customer preferred communication through WhatsApp messages instead of calls. Follow-up discussions remained limited because of unanswered communication attempts afterward."
#     ),

#     (
#         "6may no response 5 may no response 28 apr no response 27 apr not answering 24 apr not answering 18 apr no response 17 apr no response 15 apr not answering 14-Apr old lead will send Syllabus 14 apr no response 11 apr not answering , not answering 10 apr not answering 9 apr not answering 8 apr not answering 6 apr not asnwering 4 apr not asnwering 2 apr not asnwering 1 apr old lead from feb batch(blanks) not answering",
#         "Customer remained completely unresponsive despite repeated follow-up communication attempts over multiple dates. Previous lead history and syllabus sharing did not improve engagement or response rates."
#     ),

#     (
#         "6 apr i have registered from multiple sites i don't need this all stuffs ok bye 4 apr not asnwering 2 apr the number you are trying to call is currently busy",
#         "Customer stated no interest in pursuing additional course opportunities after registering through multiple platforms. Follow-up communication remained unsuccessful because of unanswered and busy calls."
#     ),

#     (
#         "20-Apr given demo video on Whatsapp 18 apr middle of a call 17-Apr send invite 15-apr not answering 9 apr texted \"Fees is too much high\" 2 apr he said he is in a meeting so you can share the syllabus and call me after few mins so we can discuss later after me going through it",
#         "Customer reviewed syllabus and demo materials but expressed strong pricing concerns during discussions. Meetings and unanswered follow-ups delayed further enrollment communication afterward."
#     ),

#     (
#         "4 apr i am out can you call me tmr 2 apr no response",
#         "Customer requested a callback for the following day because of unavailability. Earlier follow-up attempts received no response from the customer."
#     ),

#     (
#         "5 may not interested 29 apr call declined 28 apr not answering 27 apr no response 25 mar not answering 24 apr no response 21-Apr No Response 18 apr no response 17-Apr Naveen send the invite 17 apr he was outside and there was alot of noise around him , i couldn't hear anything and he disconnected 15 apr call declined 11 apr no response 10 apr not asnwering 4 apr went through the syllabus 2 apr not answering",
#         "Customer initially reviewed the syllabus but later expressed no interest in enrollment. Repeated follow-up attempts resulted in declined calls, disconnections, and no responses afterward."
#     ),

#     (
#         "6 apr ya i know but right now i am busy with other thingd and i am not looking for this i have spoke to some person alsoCustomer declined enrollment because of high pricing and other personal priorities. Meetings and voicemail responses limited further communication and follow-up discussions. its actually too costly too so i am nit rpoceeding this further 4 apr voice mail 2 apr in a meeting",
#         "Customer declined enrollment because of high pricing and other personal priorities. Meetings and voicemail responses limited further communication and follow-up discussions."
#     ),

#     (
#         "17 apr its not needed there's no use of doing thing i even texted not needed thank you 15-apr no response 15 apr he texted not needed anymore its not feasible thank you 11 apr no response 10 apr no response 4 apr i am out with my family you can share me the curriculum and details i will call you after few hours after seeing 2 apr call declined",
#         "Customer clearly expressed disinterest and stated the course was not feasible currently. Family commitments and repeated unanswered follow-ups delayed further communication."
#     ),

#     (
#         "13may-busy 12may-sent syllabus again 11may-no response 9may-no response 8may-no response 7-May sent Syllabus, Demo and Youtube again 5 may sent syllabus. he didnt have time to go through it on call, has a meeting 29 apr no response 27 apr no response 25 apr no response 24 apr not answering 18 apr no response 17 apr not answering 15-Apr no respone 11 apr currently busy 10 apr no response 8-Apr Naveen had a long discussion he is in between Jobs,etc 8 apr no response 6 apr no response 4 apr yes i ahve registered and i am willing to join but if you don't mind call me tom at 1-1:30 pm 3-apr line busy 2 apr your call is waiting as the number you have dialed is busy",
#         "Customer initially showed interest and attended detailed syllabus discussions regarding career transition opportunities. Repeated follow-ups later received no responses because of busy schedules, meetings, and job-related commitments."
#     ),

#     (
#         "5 may busy 18 apr travelling can't join 17 apr no response 10 apr voice mail 4 apr he is a data enginner and wants to know howit will help him and all i said i will connect you withh the technical team , shared intermediate course 2 apr call declined",
#         "Customer was unavailable due to travel, busy schedule, and unanswered follow-up attempts. Technical guidance and intermediate course details were shared for further evaluation."
#     ),

#     (
#         "13may-no answer 12may-busy 11may-no response 9may-busy 8may-busy 7may-getting ready for office. call around 7-730 6may-busy 28-Apr busy in travel 27-Apr Naveen send whatsapp message 23-Apr Tech Writer resend syllabus again 21-Apr Naveen send syllabus again 18 apr no response 17 apr caall declined 15 apr in office right now call after 7 10 apr currently busy 2 apr he said he is actually in office so he can't talk so just send me all the details i can do the googling and then we can connect",
#         "Customer remained consistently busy due to office work and travel commitments during follow-ups. Syllabus materials were repeatedly shared, but meaningful enrollment discussions stayed pending afterward."
#     ),

#     (
#         "10 apr no response 6 apr went through the syllabus he is thinking of may end not now 2 apr no responseb 2 apr call after 5:30",
#         "Customer reviewed the syllabus and planned to consider enrollment by the end of May. Follow-up communication remained limited because of unanswered calls and delayed responses."
#     ),

#     (
#         "2 apr the number you are trying to reach cannot receive incoming calls",
#         "Customer communication could not continue because the phone number was unable to receive incoming calls. Further follow-up attempts remained unsuccessful afterward."
#     ),

#     (
#         "6 apr call after 2-3 months 4 apr call in the vening 2 apr not asnwering",
#         "Customer requested follow-up after two to three months because of current priorities. Earlier communication attempts received delayed responses and unanswered calls."
#     ),

#     (
#         "13may-no response 12may-no response 11may-no response 9may-no response 8may-no response 7may-no response 5 may busy 29 apr not answering 27 apr no response 24 apr call declined 21-Apr not answering 17 apr currently busy 15 apr middle of a call 11 apr went through the syllabus , and fees 11 apr not answering 10 apr no response 9 apr no response 8 apr call declined 6 apr not asnwering 4 apr not asnwering 2 apr not answering 2 apr having meeting in few mins call me tmr morning",
#         "Customer reviewed syllabus and fee details but remained mostly unavailable afterward. Repeated follow-up attempts resulted in unanswered calls, declined communication, and busy schedules."
#     ),

#     (
#         "27-April Naveen send whatsapp message 23-Apr she said she needs time. 15-Apr 1.99, 16999 for AWS and AI 25k given she has no job 10 apr call declined 2 apr she has no job and it is too costly so it won't help her",
#         "Customer required additional time because of unemployment and affordability concerns regarding course pricing. WhatsApp follow-ups and discounted offers were shared during enrollment discussions."
#     ),

#     (
#         "5 may he picked up and cut the call, sounded like he was outside. he didnt respond in english 4 may- no response 4 may call at 130 and do syllabus walk through 2 may switched off 27 apr no response 25 not answering 16 apr currently busy 14 apr call declined 11 apr no response , call declined 10 apr currently busy 9 apr no response 8 apr currently busy 6 apr not answering 4 apr not asnwering 3-apr call at 1:30 Pm 2 apr call declined",
#         "Customer communication remained inconsistent with repeated unanswered and declined calls. Language barriers, busy schedules, and switched-off phone status delayed meaningful follow-up discussions."
#     ),

#     (
#         "6 apr texted not interested don't call me 4 apr number not on whatsapp 4 apr went through syllabus , needs ffes details and other details 3-Apr call in 1.5 hours 2 apr i am in office till 9pm if you can call me tmr early morning arounf 8:30 or else just drop a mail",
#         "Customer initially reviewed syllabus details and requested fee-related information through calls and email communication. Later expressed no interest and requested discontinuation of further follow-up discussions."
#     ),

#     (
#         "3- Apr Line busy 2-Apr Naveen to call tommorow he is on leave tommorow",
#         "Customer communication attempts were delayed because of busy phone lines and scheduling conflicts. Follow-up discussion with Naveen was planned for the following day."
#     ),

#     (
#         "wrong number",
#         "Customer contact information was invalid because the provided number was incorrect. Further communication and follow-up discussions could not proceed successfully."
#     ),

#     (
#         "8 apr he has just completed his studies and has no experience , i told him about the system design course 6 apr not answering 4 apr not asnwering 3-Apr line busy 2 apr currently busy",
#         "Customer recently completed studies and explored system design learning opportunities for career growth. Follow-up communication remained limited because of busy schedules and unanswered calls."
#     ),

#     (
#         "5 may said he didnt register 10 apr not asnwering 2 apr he has 1.5 years of exp told him about intermediate and system design traning",
#         "Customer has 1.5 years of experience and received guidance on intermediate and system design training options. Later denied registration and remained unavailable for further follow-up communication."
#     ),

#     (
#         "13may-voicemail 12may-voicemail 11may-voicemail 9may-voicemail 8may-voicemail 7mayvoicemail 5may voicemail 30 apr voice mail 29 apr voice mail 27 apr voice mail 16 apr voice mail 14 apr voice mail 11 apr no response , voice mail 10 apr call tmr around 5 9 apr voice mail 8 apr voice mail 6 apr voice mail 4 apr currently busy 3-Apr no response 2 apr i am a little busy right now i will call you later or tmr",
#         "Customer communication attempts consistently redirected to voicemail or received no response. Busy schedules and delayed callbacks prevented meaningful follow-up discussions and engagement."
#     ),

#     (
#         "5 may not inerested and cut the call 24 apr not a good time 16-Apr Naveen send invite 15 apr not interested and disconnected 10 apr not a good time bye 4 apr went through the syllabus , he asked sbout the fees 3-Apr Will call back in 15 mts, middle of something",
#         "Customer initially reviewed syllabus and discussed fee-related concerns during follow-ups. Later expressed disinterest, disconnected calls, and avoided further enrollment communication."
#     ),

#     (
#         "4 apr wrong number",
#         "Customer contact information was invalid because the provided number was incorrect. Further follow-up communication could not continue successfully."
#     ),

#     (
#         "5 may not interested 17 apr meet and discuss 15 apr no response 11 apr went through the syllabus 11 apr currently busy , 10 apr no response 8 apr he just doing hm hm hm not responding to anything else 4 apr not answering",
#         "Customer initially reviewed the syllabus and participated in enrollment discussions. Later expressed disinterest and remained unavailable for further follow-up communication."
#     ),

#     (
#         "14 apr temporary out of service 11 apr no rsponse , not answering 10 apr not answering 9-Apr no response 8 apr no response 4 apr not answering",
#         "Customer remained unreachable because the number was temporarily out of service. Repeated follow-up attempts resulted in unanswered calls and no responses afterward."
#     ),

#     (
#         "23-Apr no reponse 20-Apr no response 17-Apr Naveen has send the invite 15-Apr 1.99 L given need time to think about it 15 apr texted me i can't afford this 4 apr out of station for a week you can call me on next monday meanwhile you can share details on my whatsapp if i got time i will be seeing it",
#         "Customer required additional time because of affordability concerns and financial limitations. WhatsApp details and invitations were shared, but follow-up communication later received no response."
#     ),

#     (
#         "17 apr no response 16-Apr Syllabus to be send he is busy hence had a brief discussion 16 apr not answering 14 apr no response 11 apr no response , no response 10 apr right now i am busy i will connect with you later 9 apr not answering 8 apr all lines of this routes are currently busy 4 apr i will call you back after sometimes",
#         "Customer remained mostly unavailable because of busy schedules and unanswered calls. Brief syllabus discussions occurred, but follow-up communication did not progress further afterward."
#     ),

#     (
#         "10 apr voice mail 8 apr went through the syllabus he is very senior and has his own startup, 4 apr voice mail",
#         "Customer reviewed the syllabus and discussed learning opportunities despite being highly experienced with his own startup. Follow-up communication mostly resulted in voicemail responses afterward."
#     ),

#     (
#         "5 may no response 4 may busy 2 may not answering 27 apr not answering 22-Apr old lead 16 apr no response 14 apr not answering 11 apr not answering , not answering 10 apr call declined 9 apr not answering 8 apr not answering 4 apr not answering",
#         "Customer remained mostly unresponsive despite repeated follow-up communication attempts. Busy schedules, declined calls, and unanswered responses delayed further engagement discussions."
#     ),

#     (
#         "28-Apr no response 27-Apr Naveen given a demo video 22-Apr Naveen send Demo Video 20-Apr no response 15-Apr not picking call 10 apr he said evrrything is nice but fees is not in budget also this month it is working hard i told him i will check for discounts if available mostly futute batch we won't he said yes please tell me the final price i will decide based on that 4 apr went through the syllabus",
#         "Customer reviewed the syllabus and appreciated course quality but considered fees outside current budget. Demo videos and discount discussions continued, though follow-up responses remained limited afterward."
#     ),

#     (
#         "29-April call her on May-24 29 apr i am not bothered about discounts i can jin i am very busy that's the problem and disconnectd 27 apr no response 25 apr no response 24 apr not answering 21-Apr Naveen to send sylalbus again along with Youtube and Demo Video 17 apr busy with my household thing no time and no money because marriage in house okay not affordable 15-apr line busy 15 apr call after sometime 10 apr not answering 4 apr went through the syllabu s",
#         "Customer reviewed the syllabus but remained busy with household responsibilities and financial constraints. Demo videos and follow-up materials were shared, though communication stayed inconsistent afterward."
#     ),

#     (
#         "14 apr went through the syllabus 11 apr can you send me the location of office i am here and i said why and then he said i thought someone else i will call you later mam i am outside 11 apr not answering 10 apr no response 9 apr currently busy 8 apr not answering 4 apr no response , no response",
#         "Customer reviewed the syllabus but remained mostly unavailable for follow-up discussions afterward. Busy schedules, unanswered calls, and communication confusion delayed further engagement progress."
#     ),

#     (
#         "4 apr cannot recieve incoming calls",
#         "Customer communication could not continue because the phone number was unable to receive incoming calls. Further follow-up attempts remained unsuccessful afterward."
#     ),

#     (
#         "8may-said his son is using his phone so his son registered he didnt. when i told that hes spoke to naveen before, he said he's not looking for anything right now, not interested 7may-busy 6may-no answer 29-Apr line busy 28-Apr no response 24-Apr no response 23-Apr Naveen send syllabus again he will said he will check and come back . 1,99 given Als come out of Services companies 21-Apr naveen send details 14-Apr Naveen had a discussion syllabus to be given 14-Apr has given Husbands number and ask to call tommorow 9502434566 14 apr voice mail 10 apr my husband has registered i have no exp 9 apr voicemail 6 apr registered for my husband i don't know do one thing call me afterwards i will speak to him and let you know 4 apr voicemail 4 apr not asnwering",
#         "Customer communication mainly involved spouse-related discussions regarding registration and course interest. Later clarified no current interest, while repeated follow-ups resulted in voicemail responses and unanswered calls."
#     ),

#     (
#         "13may-no response 12may-no response 11may-no response 9may-no response 8may-no response 7may-no response 29 apr no response 27 apr mo response 25 apr not answering 24 apr no response 15 apr he will go through the syllabus today and come back 10 apr no response 4 apr he is a softwae developer , wants to upskill since he is learnng new technologies gen ai , how to agents and all but wants to learn more 4 apr please call me after sometime",
#         "Customer communication mainly involved spouse-related discussions regarding registration and course interest. Later clarified no current interest, while repeated follow-ups resulted in voicemail responses and unanswered calls."
#     ),

#     (
#         "7may-not interested 6may-busy 24 apr no response 17 apr invite sent 24 mar planning to do this in future not know which month but not now 26-Feb Naveen send the syllabus Youtube Video 25 feb naveen is in touch with him i cannot find his number on whastapp 25 feb he said he already spoke to naveen and is in touch with naveen 24 feb not answering",
#         "Customer initially planned future enrollment and discussed syllabus details with Naveen. Later became unresponsive and expressed no current interest."
#     ),

#     (
#         "13may-busy 12may-busy 11may-still hasnt gone through demo vid,yt, said he'll go through it and get back 9may-call on monday 8may-said he'll go through the syllabus and demo vid, then see if hes interested 7-May sent Syllabus and demo video 7may-other priorities needs some time to think and get back 6may-no answer 29 apr let me think about it i will call you 24 apr not answering 20-Apr Naveen send all demo video and Syllabus again 17 apr he has othe rstuffs to do 28 mar right now not possible i have t o save some money so right now i can't and disconnected 23 feb nthg is stopping the course is very good i was interested also but at the moment i am not in a position to pay that much amount i told him we don't take full payments you don't have to pay the complete fees at a time he said ya i know but right now creadit card is also having some issues i will take it by the end of march you call be in march 19 feb no response 13 feb call declined 12 feb no response 5 feb call declined 04 feb call declined 04 feb call declined 03 feb not ansswering 02 feb not answering 31 jan i am outside you call me tomorrow 27 gave discounts 1.99 he said give me some time by the end of the week he will decide and let us know 27 everything seems pretty good but currrently i am busy and not in a position to pay that much money i said him there you have to invest he said ya but also i am running busy i think give me sometime i will think no discount given 22 jan give me sometime i will think about it by weekend call me on monday 20 jan give me 2 3 days i am running busy i will get back to you 19 jan he said before going to the syllabus i have to think right it is like 3.5l so i will think you share me details then we will go the syllabus part , i told him we can work on discounts if you are really interested but not now , he said okay you share i will look at it",
#         "Customer showed interest in the course and reviewed syllabus, demo videos, and discounts. Financial constraints, busy schedules, and delayed responses postponed enrollment decisions repeatedly."
#     ),

#     (
#         "24 apr i am travelling and i have changed my mind don't call me 4-Apr he is interested in hospital call on Monday 15 jan not answering 13 jan not answering 20 dec he is interested he wants to know discount and when the next batch is starting 21-Nov he told that he is not able to adjust that much of amount so he told i will join next batch 17-Nov not answering 17-Nov no response 14-Nov no response 12-Nov 2.1 L provided he wants link to Demo Video and wants a days time to decide 10-Nov goen through the syllabus in brief he told fees is high he want to know the timing of the class and also he told if it is morning class on saturday and sunday it will be good for him .",
#         "Customer initially showed interest after reviewing syllabus, demo videos, pricing, and batch timings. Later declined enrollment due to travel, financial concerns, and changing priorities."
#     ),

#     (
#         "15 apr last month i have joined somewhere else 13-Nov he told he is thinking to take the course in April 10-Nov goen through syllabus he told to share syllabus 10-Nov not answering 8-Nov not answering",
#         "Customer initially considered enrolling and reviewed syllabus materials during earlier discussions. Later confirmed joining another institute, ending further enrollment interest and follow-up communication."
#     ),

#     (
#         "11may-no response 9may-no response 8may-no response 6may-no response 27 apr no response 25 apr curently busy 24 apr call me later 10 apr speaking to someone else 6-Apr send him intermediate syllabus . He has Career Gap of 2 years and financial issues",
#         "Customer received intermediate syllabus guidance despite career gap and financial concerns. Repeated follow-up attempts later resulted in busy schedules and no responses."
#     ),

#     (
#         "12may-no response 11may-no response 9may-no response 8may-no response 7may-no response 27 apr no response 17 apr call declined 16-Apr Send him intermeidate 16 apr currently busy 14 apr not answering 11 apr call declined , no response 10 apr currently busy 8 apr no response 6 apr call after 7",
#         "Customer received intermediate course guidance but remained mostly unavailable afterward. Repeated follow-up attempts resulted in busy schedules, declined calls, and no responses."
#     ),

#     (
#         "4 may sent syllabus, didnt have time for syllabus walk through 2 may not answering 27 apr not answering 25 apr call declined 21 apr no response 16 apr no response 14 apr not reachable at the moment 11 apr we can talk about tgis tmr at 2pm 10 apr not answering 9 apr not answering 8 apr no response 6 apr not answering",
#         "Customer received syllabus materials but lacked time for detailed walkthrough discussions. Repeated follow-up attempts resulted in unanswered calls, declined communication, and temporary unavailability."
#     ),

#     (
#         "6 apr wrong number",
#         "Customer contact information was invalid because the provided number was incorrect. Further communication and follow-up discussions could not proceed successfully."
#     ),

#     (
#         "13may-busy 12may-busy 11may-no response 9may-no response 8may-no answer 7may-didnt have time. sent syllabus on whatsapp said he'll respond on whatsapp if interested 6may-no response 28-Apr no response 24 apr no response 23-Apr no response 20-Apr no response 6-Apr Naveen had a long discusion and told will call him after 5 to 6 hours to join current batch",
#         "Customer initially attended detailed discussions and received syllabus materials through WhatsApp communication. Repeated follow-up attempts later received no responses because of busy schedules and limited availability."
#     ),

#     (
#         "13may-no response 12may-no response 11may-no response 9may-no response 8may-told to call back later 7may-no response 6may-not interested 30 apr busy he is in a event call later 23-Apr he wants to know timing so whatsapped him 20-Apr Naveen said offer will end soon, he said okay need time to think call on Thursday 17 apr invite sent 15-Apr 1.99 , 25K given . Syllabus sent again 9-Apr Product Manager Naveen had a syllabus walkthrough apr voicemail 8 apr currently busy 6 ap no response 6 apr call after 2pm",
#         "Customer attended syllabus walkthroughs and discussed pricing, timings, and enrollment offers during follow-ups. Later expressed disinterest and remained mostly unavailable for further communication afterward."
#     ),

#     (
#         "6may-said to call next week, didnt seem interested kept saying hmhmhm 30 apr he is travelling needs more time and he will let us know 29 apr no response 27 apr he will tell by tmr 25-Apr 1.99 given by Renu, he has asked for one live training class 25 apr wants to attend a real class , he wants to see how it is done 24 apr call me after sometime i am driving 8-Apr Old lead told him after Cloud and Agentic AI .Give both syllabus 6-Apr Line busy",
#         "Customer requested live class demonstrations and additional time before making enrollment decisions. Travel, busy schedules, and delayed responses slowed further communication."
#     ),

#     (
#         "8may-busy 7may-told to call on friday 23-Ap Naveen shared syllabus again along with Demo Video 15-Apr call tommorow same time 9 apr went through the syllabus and everything then he said fees is acrually very high i just look for courses which will cost 12000, 8000 and i also hold 14 years of exp so we can you we just look for some freshup not some end to end courses and i have recently joined a ai course which is for 8000 same trainer also have very good exp and the batch is also 15-20 people that way , it is very costly actually i said i understand but you see the value you know that architects are very highly paid ya i understand your poin but my budget should also match right ok share details no issues but i will not be to able to join 9 apr call declined 8-Apr call tommorow 1PM 6 apr call tmr at 11am",
#         "Customer reviewed syllabus details but considered course pricing beyond budget expectations. Demo materials were shared, though customer declined enrollment due to affordability concerns."
#     ),

#     (
#         "20 apr i have no money whatever discount you give 2 apr he said he might think of the next batch not this batch he is confused which course to take 28 mar not asnwering , texted him on whatsapp 27 no response 25 mar he wants to speak to naveen 25 mar intermediate course sent 25-Mar give him intermedidate course 24 mar i have discussed its tough for me 23 mar demo video shared 23 mar he is not interested because price is too high and 1lakh is also tough for him 21 mar he will join it 16 mar not answering 11 mar went through the syllabus trainer eveyrthing and then he asked about fees i told about all the courses and then he said you are charging more i am not ready to pay that much amount and then i said right now we are working on discount syou see the course no a regular course you get in the market , and i said you attend our free session on 21st you will get to know he said 21st is too far actually you don't have any other demo i said okay i can sent you the demo video he said ya okay share with me i will think about it",
#         "Customer reviewed syllabus, demo videos, and pricing but considered fees unaffordable. Financial concerns, course confusion, and inconsistent responses delayed enrollment decisions repeatedly."
#     ),

#     (
#         "13-Nov he told he is thinking to take the course in April 10-Nov goen through syllabus he told to share syllabus 10-Nov not answering 8-Nov not answering",
#         "Customer reviewed the syllabus and planned enrollment for a future batch in April. Follow-up communication remained limited because of unanswered calls afterward."
#     ),

#     (
#         "11may-said hes gone through the syllabus but not interested 9may-busy 8may- said he didnt register but attended the session by naveen. he said he'll call later 7may-no response 6may-busy 29 apr nthg is acutually structured i have to thing about it 24 apr no response 23 mar 23 mar he will talk to naveen he has his number he has questions related to interviews 11 mar ramadan is going on also he is preparing for many things he is thinking of april batch not now 11 mar not answering 26-Feb Naveen's send whatsapp message 25 feb the syllabus everytging is fantastic i have observed everything is good but see this is not what i am looking for i want something job oriented and something like dot net architecture and he mentioned 2 3 architectures see that is what i want that will cover what i am actually needing i am an egineering wants to be good in some teah lead role or something so that's why i am stepping back but okay let me think again about it 24 feb no response 20-Feb Naveen send whatsapp 19-Feb 1.99 given on whatsapp 18-Feb he whatsapped he will come back 16-Feb 2.25 given no agentica AI needed he said he will come back 11-Feb Naveen send whatsapp to understand his query 7-Feb no response 6 feb he texted me course duration is 3 months hoe come some organization like scaler takes 12 months to complete this syallbus 4-Feb Naveen had a long discussion and went over syllabus also",
#         "Customer actively reviewed syllabus details and discussed career-oriented learning expectations extensively. Later expressed disinterest because the curriculum did not align with specific job-focused goals."
#     ),

#     (
#         "12may-no response 11may-no response 9may-no response 8may-no response 7may-no response 6may-no response 30 apr no response 29 apr no response 25 6:30 no response 25 apr call in the evening 24 apr in a meeting call after 5pm , no response 21 apr in a meeting 15-Apr call after 6PM 10 apr not asnwering",
#         "Customer remained consistently unavailable despite repeated follow-up communication attempts. Meetings, delayed callbacks, and unanswered calls prevented further enrollment discussions."
#     ),

#     (
#         "13 jan another 1month i can't proceed with it thanks i will update once when i can 17-dec He said i am travelling i can't now i need more time , i said him the batch is going to start by 25th its a good time to block your seat he said no no i am travelling i can't for 2 months i said its just on weekends you can make time for it because these skills are high income skills and market is very stiff now you have already got an discount it would be a great , he said no no i am really travelling so i can update you feb 1st but right now i can't take noe 17-Nov he told in their office also they are providing training so he will come back in next month he told he will be in touch with this number 17-Nov no respone 14-Nov no response 13-Nov includig Agentic AI 2.75 he said he will update End of the Day 12-Nov naveen called he told to call later. 12-Nov he told he want to know about the certificate and told fees is high 11-Nov he told he is meeting he will call back he told me to share syllabus",
#         "Customer showed initial interest but delayed enrollment because of travel and existing training commitments. Pricing concerns and scheduling conflicts slowed further decision-making discussions."
#     ),

#     (
#         "12may-voicemail 11may-voicemail 9may-voicemail 8may-voicemail 7may-voicemail 29 apr voice mail 27 apr voice mail 24 apr voice mail 17 apr not answering 10 apr currently busy 7-Apr had a discussion",
#         "1. Customer communication mostly resulted in voicemail responses and unanswered follow-ups. Earlier discussions occurred, but meaningful engagement did not continue afterward."
#     ),

#     (
#         "17 apr no response 8 apr went through the syllabus, mostly i am looking for AI Agentic 7-Apr no response",
#         "Customer reviewed the syllabus and showed specific interest in AI Agentic learning opportunities. Follow-up communication later received no response from the customer."
#     ),

#     (
#         "8may-sent syllabus,yt vid,price. he seems interested 7may-no answer 27 apr no response 25 apr once i reach home i will call you 24 apr is in train call him after 2 -3 on saturday 17 apr no response 10 apr i am in a meeting i will call you 7-Apr Naveen had a syllabus walkthrough",
#         "Customer attended syllabus walkthroughs and received pricing, demo videos, and learning materials. Busy schedules and delayed callbacks slowed further enrollment discussions."
#     ),

#     (
#         "7may-fees is too high, not interested even with discount 6may-no response 29 apr no response 23-Apr no response 20-Apr no response 17 apr no response 15 apr given discount 1.99 15 apr texted fees 9-Apr naveen had a brief discussion he had some office call. we will send syllabus we said he directly asked fees 9 apr call declined 8 apr currently busy 7-Apr no response",
#         "Customer discussed fees and discounts but considered pricing too expensive currently. Repeated follow-up attempts later resulted in no responses and declined calls."
#     ),

#     (
#         "4may-call failed 21-Apr line busy 15-Apr call after 6PM 14-Apr number switched off 11 apr wants to connect with the technical team 10 apr not answering 9 apr call declined 8-Apr call in second half",
#         "Customer requested technical team connection for additional course clarification discussions. Communication remained inconsistent because of switched-off numbers and failed calls afterward."
#     ),

#     (
#         "11may-no response 9may-switched off 8may hes sick. send syll,yt,price. will go through and get back 7may no response 29 apr no response 27 apr not answering 24 apr no response 23-Apr he asked to resend syllabus so Naveen send it again 20-Apr Naveen had a syllabus walkthrough 16 apr not answering 14 apr no response 11 apr not answering 10 apr no response 9 apr not answering",
#         "1. Customer attended syllabus walkthroughs and requested learning materials multiple times during follow-ups. Repeated communication attempts later received no responses and unavailable contact status."
#     ),

#     (
#         "20 apr not able to pay 20k also 15-Apr discount given 1.99, 25k and 16.99K 10 apr first say course fees then we will talk , i said let me first give you a overview of the course we can discuss fees later no first fees then i said him the fees he disconnected 9 apr speaking to someone else 9 apr i am outside i will call you back later",
#         "Customer focused mainly on course fees and disconnected during pricing discussions. Financial limitations and inability to pay delayed further enrollment communication."
#     ),

#     (
#         "22-Apr Mostly will have to move him to Charity Offer. 20-Apr Naveen given offer in whatssapp 15-Apr Naveen had a walkthrough of Syllabus and asked him to join the free event , He does not have Job 10-Apr he is driving now will call back Naveen 9 apr went through the syllabus said about the trainer everything then he asked about the fees i told him all the fees then he said 3.5 lakhs is pretty huge amount i can't proceed this further i will look for something else , i said later we can work on discounts no no then too in lakhs only it will hold i can;t sorry 9 apr in a meeting call me after 3 0r 2",
#         "Customer reviewed syllabus and trainer details but considered pricing unaffordable currently. Discount and charity offer discussions continued because of unemployment and budget concerns."
#     ),

#     (
#         "11may-no response 9may-will go through syllabus and get back 8may-in office. sent syllabus on whatsapp 7may-no answer 27 apr no response 24 apr no response 23-Apr no response 20-Apr naveen had a syllabus walkthrough and informed about services business. 9-April Naveen will call you at 3Pm",
#         "Customer reviewed the syllabus and planned enrollment for a future batch in April. Follow-up communication remained limited because of unanswered calls afterward."
#     ),

#     (
#         "4 may not answering 2 may not answering 27 apr not answering 25 apr no response 16 apr currently busy , no response 14 apr speaking to someone else 11 apr in a marriage call me on monday 10 apr the number you have dailed is currretly busy, no response 9 apr speaking to someone else , same 9 april speaking to someone else",
#         "Customer remained mostly unavailable because of busy schedules and unanswered calls. Communication attempts frequently connected to someone else or busy numbers."
#     ),

#     (
#         "27-April Naveen on touch on whatsapp 14-April No response Naveen will call",
#         "Customer communication continued mainly through WhatsApp follow-ups with Naveen. Earlier follow-up attempts received no response from the customer."
#     ),

#     (
#         "21-Apr NO job can move to Charity offer 17 apr has registered 15 apr texted syllabus is good 14-Apr Naveen had a Syllabus Walkthrough with him. 14 apr not answering 11 apr not answering , no response",
#         "Customer attended syllabus walkthroughs and appreciated course content during discussions. Unemployment concerns led to consideration for charity-based enrollment offers."
#     ),

#     (
#         "11may-no response 9may-no response 8may-no response 7may-no response 27 apr no response 20-Apr no respose 16 apr currently busy , no response 14 apr speaking to someone else 11 apr in a marriage call me on monday 10 apr the number you have dailed is currretly busy, no response 9 apr speaking to someone else , same 9 april speaking to someone else",
#         "Customer remained mostly unavailable despite repeated follow-up communication attempts over multiple dates. Calls frequently connected to others, busy numbers, or received no responses afterward."
#     ),

#     (
#         "11may-no response 9may-no response 8may-no response 7may-no response 27 apr no response 15-Apr no response 13-Apr send the syllabus 11 apr call me in the evening",
#         "Customer initially requested syllabus details and preferred evening follow-up communication. Repeated follow-up attempts later received no responses from the customer."
#     ),

#     (
#         "25 apr don't want to know discounts and not interested 21-Apr Naveen had a syllabus walkthrough 15-Apr call him on Saturday 13-Apr Call Tommorow Morning",
#         "Customer attended syllabus walkthrough discussions and scheduled follow-up callbacks for further communication. Later expressed disinterest and declined discount-related enrollment discussions."
#     ),

#     (
#         "4 may automated voicemail 2 may automated voicemail 27 apr no response 21-Apr no response 16 apr not answering 14 apr not answering , no response",
#         "Customer communication attempts mostly resulted in automated voicemail and unanswered responses. Follow-up discussions could not progress because of repeated unavailability and no engagement."
#     ),

#     (
#         "16-Apr does not fit it int our course (analyst) 16 apr not answering 15 apr no response 14 apr no response, no response",
#         "Customer profile was identified as unsuitable for the current course requirements. Repeated follow-up attempts later received no response from the customer."
#     ),

#     (
#         "22-Apr he never picks call 21 apr voicemail 16 apr no response 15 apr no response",
#         "Customer consistently remained unreachable and did not respond to follow-up communication attempts. Calls frequently redirected to voicemail without meaningful engagement afterward."
#     ),

#     (
#         "25 apr cost is too high don't conract 15 apr went through the syllabus , he asked fees",
#         "Customer reviewed the syllabus and discussed fee-related details during enrollment conversations. Later declined further communication because the course cost was considered too high."
#     ),

#     (
#         "4 may cannot receive incoming calls 2 may currently busy 27 apr currently busy 17 apr no response 16 apr not answering , call declined 15 apr some lady picked the call , she is just saying hlo hlo and then declined",
#         "Customer remained mostly unavailable because of busy schedules and unanswered calls. Communication issues, declined calls, and unreachable numbers delayed further follow-up discussions."
#     ),

#     (
#         "11may-no response 9may-busy 8may-busy 7may-no response 27 apr no response 23-Apr he has not gone over the syllabus 21-Apr Naveen had a syllabus walkthrough and come out of services companies 17 apr no response 16 apr not answering , no response 15 apr not answering",
#         "Customer attended syllabus walkthrough discussions regarding transitioning from service-based roles and career growth opportunities. Follow-up communication later received no responses because of busy schedules and lack of syllabus review."
#     ),

#     (
#         "15 apr i am not pradeep, recently i have got this number from my company previously it was used by pradeep",
#         "Customer clarified the contact number now belongs to a different employee and not the original lead. Further follow-up communication for the previous customer could not continue."
#     ),

#     (
#         "20-Apr budget only 10k then recorded trainings will help here only at 39.9 and other parts AWS and agentic AI will be discounted 17 apr he will do by evening 15-Apr Naveen had a Syllabus Walkthrough",
#         "Customer attended syllabus walkthrough discussions and explored budget-friendly training options. Financial constraints limited enrollment interest, while discounted recorded and AWS training alternatives were suggested."
#     ),

#     (
#         "8may-he doesnt have time to do the course, said hes not interested 7may-no response 6may-no response 24 apr currently busy 17 apr no response 2-Apr no response 24- Mar ouside of netowrk coverage , Naveen send whataapp 23-Mar offer given of 2.25 including AgentIc AI and AWS 16999, he asked Naveen to send syllabus 21 mar not answering 16-Mar No response 9-March Naveen had a syllabus walkthrough",
#         "Customer attended syllabus walkthrough discussions and received pricing details including AWS and Agentic AI offerings. Later expressed disinterest because of time constraints, unavailability, and inconsistent follow-up responses."
#     ),

#     (
#         "6-May he is not well 28-April Naveen given the demo video 27-April Will decide later today 24-April He said to whatsapp on 8310624604 all details he was checking how many jobs people got,etc 23-April Naveen had a sylalbus walkthrough and told him to upskill and come out of services companies . Naveen said he will see if a discount can be given as of now none and also next batch we might put 18% GST . He wants to be in touch in future also 19 apr not answering",
#         "Customer attended syllabus walkthrough discussions and explored career upskilling opportunities with future batch considerations. Health issues, delayed decision-making, and inconsistent follow-up responses slowed enrollment progress afterward."
#     ),

#     (
#         "25 apr I understand discount is good but i am really not interested i ahve other works too in future we will see i said price might increase we will charge 18% gst for the next batch yaa but then too right now i can't 18 apr went through the syllabus ,",
#         "Customer reviewed the syllabus and appreciated available discount offers during discussions. Enrollment was postponed because of other priorities and lack of immediate interest."
#     ),

#     (
#         "28-April no response 27-April he feels 1.99 L is very high he has only 1L only 22-Apr no respone 21-Apr 1.99 given , Naveen gave Demo Video also 18 apr went theough the syllabus he asked about the fees and said its acutually very difficult for me to take this only 3.5 or 4 months how you will cover i have to think probably i won't tke",
#         "Customer reviewed the syllabus and demo materials but considered course pricing unaffordable within current budget limitations. Concerns about course duration and learning coverage delayed enrollment decisions and follow-up responses."
#     ),

#     (
#         "8may-no response 7may-no response 6 may-no response 28-Apr call at 6 or 7 PM 22-Apr no response 21-Apr call tommorow at 11 AM need time 20/04/2026 Naveen had a discussion syllabus to be send out",
#         "Customer attended initial syllabus discussions and requested additional time before continuing enrollment decisions. Repeated follow-up attempts later received no responses from the customer."
#     ),

#     (
#         "20 apr not answering",
#         "Customer did not respond to follow-up communication attempts during the engagement period. Further enrollment discussions could not progress because of unavailability."
#     ),

#     (
#         "22-Apr Naveen send syllabus again 21 sent syllabus 20 apr not answering",
#         "Customer received syllabus materials multiple times during follow-up communication attempts. Earlier discussions remained inactive because the customer did not respond to calls."
#     ),

#     (
#         "4 may busy 2 may no response 27 apr no response 25 aapr middle of a call 22-Apr call at 12:50 PM 21 apr no response 20 apr no response",
#         "Customer remained mostly unavailable because of busy schedules and interrupted calls. Repeated follow-up attempts resulted in no responses and delayed communication."
#     ),

#     (
#         "12may-no response 11may-no response 9may-no response 8may-no response 7may-no response 6may-no response 24-Apr no response 21-Apr 1.99 given and Agentic AI 25k he wants with Agentic AI Naveen to send him Demo Video 20 apr went through the syllabus",
#         "Customer reviewed the syllabus and showed interest in Agentic AI learning opportunities with demo video requests. Repeated follow-up attempts later received no responses from the customer."
#     ),

#     (
#         "20 apr dialed number does not exist",
#         "Customer contact number was invalid and could not be reached successfully. Further follow-up communication attempts were not possible afterward."
#     ),

#     (
#         "4 may no response 2 may no response 27 apr not answering 25 apr no response 21 apr not answering 20 apr not answering",
#         "Customer remained consistently unavailable despite repeated follow-up communication attempts over multiple dates. Calls were unanswered and meaningful enrollment discussions could not progress further."
#     ),

#     (
#         "11may-busy 9may-no response 8may-driving 7may-busy 27 apr currently busy 25 apr huge amount after discount too give me sometimes i will think about it 22-Apr Naveen to send Youtube and Demo Video 21-Apr Naveen had a discusson on the syllabus. 21 apr no response 20 apr call tmr 20 apr driving right now call me after 4 hours right now the time is 3:00pm",
#         "Customer attended syllabus discussions and received demo video materials for further evaluation. Busy schedules, driving commitments, and pricing concerns delayed enrollment decisions and follow-up responses."
#     ),

#     (
#         "20 apr someone picked the call and said wrong number",
#         "Customer contact attempt reached a different person who confirmed the number was incorrect. Further follow-up communication with the intended customer could not continue."
#     ),

#     (
#         "11may-call after 12 9may-no response 8may-busy 25 apr call me after sometime 22-Apr no response 21-Apr Naveen had a long discussion and also told about AWS 16999, Agentic AI he does not want 21 apr not answering 20 apr in a meeting call me later",
#         "Customer attended detailed syllabus discussions including AWS and Agentic AI course offerings. Busy schedules, meetings, and inconsistent responses delayed further enrollment communication and decision-making."
#     ),

#     (
#         "21 mar currently busy 20 apr no response",
#         "Customer remained busy and unavailable during follow-up communication attempts. Further discussions could not progress because of no response afterward."
#     ),

#     (
#         "7may-busy 6may-no response 24-Apr responded on whatsapp 23-Apr Naveen had a syllabus walkthrough he is interested, no discount given he said he has some medical condition at home and see if we can pay as part payment 21-Apr busy in another call 21 apr not answering 20 apr in meeting call after 6:30, no response",
#         "Customer attended syllabus walkthrough discussions and showed interest in the program despite no discount availability. Medical issues at home, busy schedules, and delayed responses slowed enrollment follow-up communication."
#     ),

#     (
#         "4 may busy 2 may no response 27 apr i am not interested i will think about this later, i said him that you have registered for it and he disconnected 25 apr no response 22-Apr call at lunch time 21 apr not answering 20 apr no response",
#         "Customer initially registered and participated in follow-up discussions but later expressed no current interest in enrollment. Repeated communication attempts afterward received no responses and disconnected calls."
#     ),

#     (
#         "12may-no response 11may-no response 9may-no response 8may-no response 7may-no response 6may-no response 24 apr out of network coverage area 20-Apr Naveen gave syllabus and demo video",
#         "Customer received syllabus and demo video materials during the initial follow-up discussion. Repeated communication attempts later received no responses and network connectivity issues."
#     ),

#     (
#         "11may-no response 9may-no response 8may-no response 7may-no response 22-Apr Devops guy 1.99 given Naveen said he can give one teaser class on DS and Mulit threading free to jump start 20 apr went through the syllabus , asked about fees",
#         "Customer reviewed the syllabus and discussed course fees during follow-up communication. Free teaser classes and discounted DevOps training options were offered, but later responses remained unavailable."
#     ),

#     (
#         "25 apr i am doing something else so i don't have time and disconnected 21 apr not answering 20 apr no response",
#         "Customer stated involvement in other activities and expressed lack of time for the course currently. Repeated follow-up attempts afterward received no responses from the customer."
#     ),

#     (
#         "6may-no response 1-May he messaged he is in meeting will call in the evening 30-Apr naveen asked to go over Demo Videos and come out of Services companies 28-Apr he is doing Agentic AI course 27-Apr line busy 24-Apr Need one more day 23-Apr Morning 11AM he will call, 1.99 given with 25k and and 16999 for AWS 21 apr naveen had a long discussion 20 apr currently busy",
#         "Customer attended detailed syllabus discussions and reviewed pricing, AWS, and Agentic AI course options. Existing Agentic AI enrollment, busy schedules, and delayed responses slowed further enrollment decisions."
#     ),

#     (
#         "30 apr no response 29 apr call in the eve 27 apr call him tmr 24 mar he will think about it call him on monday 25 mar right now i am not ready for so much investment i can consider this is future 25 mar not asnwering 23 mar no response 21 mar he will join 19-Mar he responded he is registered for the event 18-Mar he is from Avaya , Naveen had a deep discussion and syllabus walkthrough 18-Mar no response",
#         "Customer attended detailed syllabus walkthrough discussions and initially showed interest in joining the program. Investment concerns, delayed callbacks, and repeated unanswered follow-ups later slowed enrollment progress."
#     ),

#     (
#         "11may-no response 9may-voicemail 8may-voicemail 7may-voicemail 6may-voicemail 29-Apr Naveen send syllabus again he is not having bandwidth 2-Apr busy with deleveriables 21 mar i was telling him he declined in the middle and now not answering 16-Mar he is interested but no bandwidth Naveen gave 1.99 offer and told him to join April batch he said he can conisder this and will join the April mostly. Naveen will contact end of March again 14 mar he picked the call i said am i speaking to hari krihsna he said yes and then he disconnected now he is not answering 12 mar not yet please i can think about this on weekends 10 mar he said i am driving and don't have a lot of time just send the details on my whatsapp 7 mar currently busy 5 mar call me after 2 days he is out 4 mar call me after 12:30 3-March he is busy call later 6:07 no response 2 march he is busy and stuck in the traffic so he said can you call sometime in th evening",
#         "Customer initially showed interest after detailed syllabus discussions and discounted enrollment offers. Busy schedules, voicemail responses, and lack of bandwidth delayed further communication and enrollment confirmation."
#     ),

#     (
#         "13-May Naveen send whatsapp messsage Ping him on May-10th",
#         "Customer follow-up communication continued through WhatsApp messaging by Naveen. Additional follow-up engagement was planned for May 10th."
#     ),

import torch
import pandas as pd
import random

SEED = 42

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# MODEL CONFIG
D_MODEL = 64
NUM_HEADS = 4
NUM_LAYERS = 2
D_FF = 128
MAX_LEN = 32

# TRAINING CONFIG
SUMMARIZATION_EPOCHS = 180
SUMMARIZATION_BATCH_SIZE = 2
SUMMARIZATION_LR = 1e-3

MAX_SRC_LEN = 128
MAX_TGT_LEN = 40

# LOAD EXCEL
df = pd.read_excel("C:/Users/cheta/OneDrive/Desktop/ForTraining.xlsx")

df = df.dropna()

SUMMARIZATION_DATA = [
    (str(row["Comments"]), str(row["Summaries"]))
    for _, row in df.iterrows()
]

print("Total Samples:", len(SUMMARIZATION_DATA))
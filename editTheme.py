# process theme files
# -*- coding: UTF-8 -*-
import os, sys, zipfile
from datetime import *
from slugify import slugify

htmlFiles = []
cssFiles = []
seoText = [
	"Designed by PrimarySite",
	"Design by PrimarySite",
	"Website by PrimarySite",
	"Web Site by PrimarySite",
	"Web Design by PrimarySite",
	"Website Design by PrimarySite",
	"Website Designed by PrimarySite",
	"Web Site Design by PrimarySite",
	"Web Site Designed by PrimarySite",
	"Websites for schools by PrimarySite",
	"Websites for primary schools by PrimarySite",
	"Primary School Websites by PrimarySite",
	"Websites for Primary Schools by PrimarySite",
	"PrimarySite School Website Design",
	"A PrimarySite School Website",
	"A PrimarySite School Website Design",
	"A PrimarySite School Web Site",
	"A PrimarySite School Web Site Design",
	"Unique Websites for schools by PrimarySite",
	"Unique Websites for Unique Schools by PrimarySite",
	"Created by PrimarySite",
	"Created by PrimarySite, school website designers",
	"Created by PrimarySite, primary school website designers",
	"PrimarySite Website Design",
	"PrimarySite Web Design",
	"School Website by PrimarySite",
	"School Website from PrimarySite",
	"School Website Design by PrimarySite",
	"School Website Designed by PrimarySite",
	"PrimarySite - Websites for Schools",
	"PrimarySite - Websites for Primary Schools",
	"PrimarySite - School Website Designers",
	"PrimarySite - the School Website Specialists",
	"PrimarySite - School Websites",
	"PrimarySite - Websites for Schools",
	"PrimarySite - Websites for Primary Schools ",
	"PrimarySite - School Web Site Designers",
	"PrimarySite - the School Web Site Specialists",
	"PrimarySite - School Web Sites",
	"PrimarySite - Web Sites for Schools",
	"PrimarySite - Web Sites for Primary Schools",
	"PrimarySite - Outstanding School Websites",
	"PrimarySite - Outstanding School Web Sites",
	"Web Site by PrimarySite",
	"Web Site Design by PrimarySite",
	"Primary School Websites by PrimarySite",
	"A PrimarySite School Website Design",
	"Unique Websites for Unique Schools by PrimarySite",
	"PrimarySite Website Design",
	"School Website Design by PrimarySite",
	"PrimarySite - School Website Designers",
	"PrimarySite - Websites for Primary Schools",
	"Created by PrimarySite",
	"PrimarySite Website Design",
]
calendarWeek = datetime.today().isocalendar()[1]
zipPath = "themes/"

def processTheme(topicNames,topicSlugs,themeslug,specialPages):
	htmlPath = "orig/html/"
	cssPath = "orig/css/"
	themePath = "themes/"
	htmlWritePath = "new/html/"
	cssWritePath = "new/css/"
	newThemePath = "new/"
	# edit html files
	htmlNames = os.listdir(htmlPath)
	for file in htmlNames:
		with open(htmlPath+file,'r') as f:
			text = f.read()
		if file == 'core.homepage.html':
			text = text.replace('{% extends "BuildTemplate/base.html" %}','{% extends "'+themeslug+'/base.html" %}')
		elif file == 'base.html':
			text = text.replace('                        {% topic_menu_full about-us "About Us" %}\n','##')
			text = text.replace('                        {% topic_menu_full key-information "Key Information" %}\n','')
			text = text.replace('                        {% topic_menu_full news-and-events "News and Events" %}\n','')
			text = text.replace('                        {% topic_menu_full parents "Parents" %}\n','')
			text = text.replace('                        {% topic_menu_full children "Children" %}\n','')
			text = text.replace('Website design by PrimarySite',seoText[calendarWeek])
			newTopics = ''
			i = 0
			while i < len(topicSlugs):
				newTopics += '                        {% topic_menu_full '+topicSlugs[i]+' "'+topicNames[i]+'" %}\n'
				i = i+1
			text = text.replace('##',newTopics)
		elif file == 'calendar.grid.html' or file == 'diary.detail.html' or file == 'diary.list.html':
			text = text.replace('Calendar',specialPages['calendarName'])
			text = text.replace('    <li><a href="{% topic_url news-and-events %}">News and Events</a></li>','    <li><a href="{% topic_url '+slugify(specialPages['calendarParent'], to_lower=True)+' %}">'+specialPages['calendarParent']+'</a></li>')
			text = text.replace('{% extends "BuildTemplate/base.html" %}','{% extends "'+themeslug+'/base.html" %}')
		elif file == 'special.calendar-breadcrumbs.html':
			text = text.replace('Calendar',specialPages['calendarName'])
			text = text.replace('<li><a href="{% topic_url news-and-events %}">News and Events</a></li>','<li><a href="{% topic_url '+slugify(specialPages['calendarParent'], to_lower=True)+' %}">'+specialPages['calendarParent']+'</a></li>')
			text = text.replace('{% extends "BuildTemplate/base.html" %}','{% extends "'+themeslug+'/base.html" %}')
		elif file == 'news.aggregate-list.html' or file == 'news.detail.html':
			text = text.replace('Latest News',specialPages['newsName'])
			text = text.replace('    <li><a href="{% topic_url news-and-events %}">News and Events</a></li>','    <li><a href="{% topic_url '+slugify(specialPages['newsParent'], to_lower=True)+' %}">'+specialPages['newsParent']+'</a></li>')
			text = text.replace('    <li><a href="{% activity_stream_url full news %}">Latest News</a></li>','    <li><a href="{% activity_stream_url full news %}">'+specialPages['newsName']+'</a></li>')
			text = text.replace('{% extends "BuildTemplate/base.html" %}','{% extends "'+themeslug+'/base.html" %}')
		elif file == 'special.brain-builders.html' or file == 'special.english.html' or file == 'special.games.html' or file == 'special.history.html' or file == 'special.ks1-links.html' or file == 'special.ks2-links.html' or file == 'special.maths.html' or file == 'special.science.html' or file == 'special.kidszone.html':
			text = text.replace('    <li><a href="{% topic_url children %}">Children</a></li>','    <li><a href="{% topic_url '+slugify(specialPages['kidParent'], to_lower=True)+' %}">'+specialPages['kidParent']+'</a></li>')
			text = text.replace('Kids\' Zone',specialPages['kidName'])
			text = text.replace('{% extends "BuildTemplate/base.html" %}','{% extends "'+themeslug+'/base.html" %}')
		elif file == 'special.sitemap.html':
			text = text.replace('            {% topic_menu_full about-us %}\n','##')
			text = text.replace('            {% topic_menu_full key-information %}\n','')
			text = text.replace('            {% topic_menu_full news-and-events %}\n','')
			text = text.replace('            {% topic_menu_full parents %}\n','')
			text = text.replace('            {% topic_menu_full children %}\n','')
			newTopics = ''
			i = 0
			while i < len(topicSlugs):
				newTopics += '            {% topic_menu_full '+topicSlugs[i]+' %}\n'
				i = i+1
			text = text.replace('##',newTopics)
			text = text.replace('{% extends "BuildTemplate/base.html" %}','{% extends "'+themeslug+'/base.html" %}')
		else:
			text = text.replace('{% extends "BuildTemplate/base.html" %}','{% extends "'+themeslug+'/base.html" %}')
		with open(htmlWritePath+file,'w') as f:
			f.write(text)
	# edit css files
	cssNames = os.listdir(cssPath)
	for file in cssPath:
		with open(cssPath+file,'r') as f:
			text = f.read()
		if file == 'homepage.css':
			text = text.replace('.main-nav .ps_topic_slug_about-us {}\n','##')
			text = text.replace('.main-nav .ps_topic_slug_key-information {}\n','')
			text = text.replace('.main-nav .ps_topic_slug_news-and-events {}\n','')
			text = text.replace('.main-nav .ps_topic_slug_parents {}\n','')
			text = text.replace('.main-nav .ps_topic_slug_children {}\n','')
			newTopics = ''
			i = 0
			while i < len(topicSlugs):
				newTopics += '.main-nav .ps_topic_slug_'+topicSlugs[i]+' {}\n'
				i = i+1
			text = text.replace('##',newTopics)
		if file == 'style.css':
			# line 129
			text = text.replace('.main-nav .ps_topic_slug_about-us { background-position: 0 -52px; z-index: 199; }\n','##')
			text = text.replace('.main-nav .ps_topic_slug_key-information { background-position: 0 -104px; z-index: 198; }\n','')
			text = text.replace('.main-nav .ps_topic_slug_news-and-events { background-position: 0 -156px; z-index: 197; }\n','')
			text = text.replace('.main-nav .ps_topic_slug_parents { background-position: 0 -208px; z-index: 196; }\n','')
			text = text.replace('.main-nav .ps_topic_slug_children { background-position: 0 -260px; z-index: 195; }\n','')
			newTopics = ''
			i = 0
			z = 199
			p = 52
			while i < len(topicSlugs):
				newTopics += '.main-nav .ps_topic_slug_'+topicSlugs[i]+' { background-position: 0 -'+p+'px; z-index: '+z+'; }\n'
				i = i+1
				z = z-1
				p = p+52
			text = text.replace('##',newTopics)
			# line 136
			text = text.replace('.main-nav .ps_topic_slug_about-us:focus, .main-nav .ps_topic_slug_about-us:hover { background-position: right -52px; }\n','##')
			text = text.replace('.main-nav .ps_topic_slug_key-information:focus, .main-nav .ps_topic_slug_key-information:hover { background-position: right -104px; }\n','')
			text = text.replace('.main-nav .ps_topic_slug_news-and-events:focus, .main-nav .ps_topic_slug_news-and-events:hover { background-position: right -156px; }\n','')
			text = text.replace('.main-nav .ps_topic_slug_parents:focus, .main-nav .ps_topic_slug_parents:hover { background-position: right -208px; }\n','')
			text = text.replace('.main-nav .ps_topic_slug_children:focus, .main-nav .ps_topic_slug_children:hover { background-position: right -260px; }\n','')
			newTopics = ''
			i = 0
			p = 52
			while i < len(topicSlugs):
				newTopics += '.main-nav .ps_topic_slug_'+topicSlugs[i]+':focus, .main-nav .ps_topic_slug_'+topicSlugs[i]+':hover { background-position: right -'+p+'px; }\n'
				i = i+1
				p = p+52
			text = text.replace('##',newTopics)
			# line 204
			text = text.replace('.main-nav .ps_topic_slug_about-us ul {}\n','##')
			text = text.replace('.main-nav .ps_topic_slug_key-information ul {}\n','')
			text = text.replace('.main-nav .ps_topic_slug_news-and-events ul {}\n','')
			text = text.replace('.main-nav .ps_topic_slug_parents ul {}\n','')
			text = text.replace('.main-nav .ps_topic_slug_children ul {}\n','')
			newTopics = ''
			i = 0
			while i < len(topicSlugs):
				newTopics += '.main-nav .ps_topic_slug_'+topicSlugs[i]+' ul {}\n'
				i = i+1
			text = text.replace('##',newTopics)
			# line 225
			text = text.replace('.main-nav .ps_topic_slug_about-us ul li a {}\n','##')
			text = text.replace('.main-nav .ps_topic_slug_key-information ul li a {}\n','')
			text = text.replace('.main-nav .ps_topic_slug_news-and-events ul li a {}\n','')
			text = text.replace('.main-nav .ps_topic_slug_parents ul li a {}\n','')
			text = text.replace('.main-nav .ps_topic_slug_children ul li a {}\n','')
			newTopics = ''
			i = 0
			while i < len(topicSlugs):
				newTopics += '.main-nav .ps_topic_slug_'+topicSlugs[i]+' ul li a {}\n'
				i = i+1
			text = text.replace('##',newTopics)
			#line 241
			text = text.replace('.main-nav .ps_topic_slug_about-us ul li:focus, .main-nav .ps_topic_slug_about-us ul li:hover {}\n','##')
			text = text.replace('.main-nav .ps_topic_slug_key-information ul li:focus, .main-nav .ps_topic_slug_key-information ul li:hover {}\n','')
			text = text.replace('.main-nav .ps_topic_slug_news-and-events ul li:focus, .main-nav .ps_topic_slug_news-and-events ul li:hover {}\n','')
			text = text.replace('.main-nav .ps_topic_slug_parents ul li:focus, .main-nav .ps_topic_slug_parents ul li:hover {}\n','')
			text = text.replace('.main-nav .ps_topic_slug_children ul li:focus, .main-nav .ps_topic_slug_children ul li:hover {}\n','')
			newTopics = ''
			i = 0
			while i < len(topicSlugs):
				newTopics += '.main-nav .ps_topic_slug_'+topicSlugs[i]+' ul li:focus, .main-nav .ps_topic_slug_'+topicSlugs[i]+' ul li:hover {}\n'
				i = i+1
			text = text.replace('##',newTopics)
			# line 249
			text = text.replace('.main-nav .ps_topic_slug_about-us ul a:focus, .main-nav .ps_topic_slug_about-us ul a:hover {}\n','##')
			text = text.replace('.main-nav .ps_topic_slug_key-information ul a:focus, .main-nav .ps_topic_slug_key-information ul a:hover {}\n','')
			text = text.replace('.main-nav .ps_topic_slug_news-and-events ul li a:focus, .main-nav .ps_topic_slug_news-and-events ul li a:hover {}\n','')
			text = text.replace('.main-nav .ps_topic_slug_parents ul li a:focus, .main-nav .ps_topic_slug_parents ul li a:hover {}\n','')
			text = text.replace('.main-nav .ps_topic_slug_children ul li a:focus, .main-nav .ps_topic_slug_children ul li a:hover {}\n','')
			newTopics = ''
			i = 0
			while i < len(topicSlugs):
				newTopics += '.main-nav .ps_topic_slug_'+topicSlugs[i]+' ul a:focus, .main-nav .ps_topic_slug_'+topicSlugs[i]+' ul a:hover {}\n'
				i = i+1
			text = text.replace('##',newTopics)
		with open(cssWritePath+file,'w') as f:
			f.write(text)
	zipName = themeslug+".zip"
	return zipName
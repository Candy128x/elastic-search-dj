# Elastic Search in Django

---
## Software Requirements
- python : 3.6.9
- django : 3.0.4


---
## Elasric Search Response
	- CMD Terminal
<kbd><img src="/imgs-readme/screenshot_from_2020-03-13_16-33-50.png" alt="django_default-page_v1-1" title="django_default-page"></img></kbd>


---
## Postman Collection Link
- elastic-search-dj
> https://www.getpostman.com/collections/381e57bbd3fcbd2404c4


---
## Postman - Customer Update Operation
```
method: PUT
URL: http://127.0.0.1:8000/customer/api/v1/3/
request: 
	{
		"name": "Deviprasad",
		"email": "dev3@gm.com",
		"contact_no": 9819123456,
		"password": "qwerty",
		"extra": {
			"country": "india",
			"txt": "0318"
		}
	}

response:
	{
		"id": 3,
		"name": "Deviprasad",
		"email": "dev3@gm.com",
		"contact_no": "9819123456",
		"password": "qwerty",
		"extra": {
			"country": "india",
			"txt": "0318"
		}
	}


```


---
## Terminal Output:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
---store_customer_updation_query--- {'name': 'Deviprasad', 'email': 'dev3@gm.com', 'contact_no': 9819123456, 'password': 'qwerty', 'extra': {'country': 'india', 'txt': '0318'}}
---store_customer_updation_query---append--- {'name': 'Deviprasad', 'email': 'dev3@gm.com', 'contact_no': 9819123456, 'password': 'qwerty', 'extra': {'country': 'india', 'txt': '0318'}, 'entity_type': 'customer', 'entity_id': 3, 'created_at': '2020-03-16 09:54:24', 'timestamp': 1584352464}
---store_customer_updation_query---es_response--- {'_index': 'customer-index-2', '_type': 'update-doc', '_id': 'Q-jE4nABVmioxhH4EAVm', '_version': 1, 'result': 'created', '_shards': {'total': 2, 'successful': 1, 'failed': 0}, '_seq_no': 4, '_primary_term': 4}
[16/Mar/2020 09:54:25] "PUT /customer/api/v1/3/ HTTP/1.1" 200 137


```


---
## Postman - Elastic Search API to fetch Customer Updated Data
```
method: POST
URL: http://localhost:9200/customer-index-2/update-doc/_search?filter_path=hits.hits._source
request: 
	{
		"query": {
			"bool": {
				"must": [
					{
						"match": {
							"entity_type": "customer"
						}
					},
					{
						"match": {
							"entity_id": 3
						}
					}
				]
			}
		},
		"sort": {
			"timestamp": {
				"order": "asc"
			}
		},
		"_source": {
			"includes": [],
			"excludes": [
				"password"
			]
		}
	}

response:
	{
		"hits": {
			"hits": [
				{
					"_source": {
						"entity_type": "customer",
						"contact_no": 9819,
						"extra": {
							"country": "india"
						},
						"name": "Deviprasad",
						"created_at": "2020-03-14 07:40:23",
						"entity_id": 3,
						"email": "dev3@gm.com",
						"timestamp": 1584171623
					}
				},
				{
					"_source": {
						"entity_type": "customer",
						"contact_no": 9819,
						"extra": {
							"country": "india"
						},
						"name": "Deviprasad",
						"created_at": "2020-03-14 07:40:23",
						"entity_id": 3,
						"email": "dev4@gm.com",
						"timestamp": 1584171623
					}
				},
				{
					"_source": {
						"entity_type": "customer",
						"contact_no": 9819,
						"extra": {
							"country": "india"
						},
						"name": "Deviprasad",
						"created_at": "2020-03-14 07:40:23",
						"entity_id": 3,
						"email": "dev4@gm.com",
						"timestamp": 1584171623
					}
				},
				{
					"_source": {
						"entity_type": "customer",
						"contact_no": 9819123456,
						"extra": {
							"country": "india"
						},
						"name": "Deviprasad",
						"created_at": "2020-03-16 09:25:41",
						"entity_id": 3,
						"email": "dev3@gm.com",
						"timestamp": 1584350741
					}
				},
				{
					"_source": {
						"entity_type": "customer",
						"contact_no": 9819123456,
						"extra": {
							"country": "india",
							"txt": "0259"
						},
						"name": "Deviprasad",
						"created_at": "2020-03-16 09:29:51",
						"entity_id": 3,
						"email": "dev3@gm.com",
						"timestamp": 1584350991
					}
				},
				{
					"_source": {
						"entity_type": "customer",
						"contact_no": 9819123456,
						"extra": {
							"country": "india",
							"txt": "0300"
						},
						"name": "Deviprasad",
						"created_at": "2020-03-16 09:30:03",
						"entity_id": 3,
						"email": "dev3@gm.com",
						"timestamp": 1584351003
					}
				},
				{
					"_source": {
						"entity_type": "customer",
						"contact_no": 9819123456,
						"extra": {
							"country": "india",
							"txt": "0300"
						},
						"name": "Deviprasad",
						"created_at": "2020-03-16 09:47:54",
						"entity_id": 3,
						"email": "dev3@gm.com",
						"timestamp": 1584352074
					}
				},
				{
					"_source": {
						"entity_type": "customer",
						"contact_no": 9819123456,
						"extra": {
							"country": "india",
							"txt": "0318"
						},
						"name": "Deviprasad",
						"created_at": "2020-03-16 09:48:20",
						"entity_id": 3,
						"email": "dev3@gm.com",
						"timestamp": 1584352100
					}
				}
			]
		}
	}


```


---

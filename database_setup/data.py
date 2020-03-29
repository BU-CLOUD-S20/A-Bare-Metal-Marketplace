import uuid
from datetime import datetime, timedelta
from dateutil.tz import gettz
import Models.marketModel as Market
import statuses


# bid_ids = []
# if len(bid_ids) == 0:
#     for i in range(0, 10):
#         bid_ids.append(uuid.uuid4())
#
# offer_ids = []
# if len(offer_ids) == 0:
#     for i in range(0, 10):
#         offer_ids.append(uuid.uuid4())
#
# project_ids = []
# if len(project_ids) == 0:
#     for i in range(0, 10):
#         project_ids.append(uuid.uuid4())
#
# resource_ids = []
# if len(resource_ids) == 0:
#     for i in range(0, 10):
#         resource_ids.append(uuid.uuid4())
#
# ny = gettz('America/New_York')
# time = datetime(2020, 3, 1, 10, 30, tzinfo=ny)
#
# tzinfo=gettz('America/New_York')
#
# start_times = []
# if len(start_times) == 0:
#     for i in range(0, 10):
#         start_times.append(time + timedelta(days=i - 1))
#
# end_times = []
# if len(end_times) == 0:
#     for i in range(0, 10):
#         end_times.append(time + timedelta(days=i))
#
#
# config = {"memory_gb": 10240,
# "cpu_arch": "x86_64",
# "cpu_physical_count": 4,
# "cpu_core_count": 16,
# "cpu_ghz": 3
# }
#
# bids = []
# for i in range(0, 10):
#     bids.append(dict(
#         bid_id=bid_ids[i],
#         project_id = project_ids[i],
#         quantity = 1,
#         start_time = start_times[i],
#         end_time = end_times[i],
#         duration = 16400,
#         status = statuses.AVAILABLE,
#         config_query = config,
#         cost = 11))
#
# print(bids)

offer0 = {'offer_id': '0ee67a67-f8e2-4db0-be81-fa9579f3ebd0', 'project_id': 'ab23f5d5-9718-4c8e-a499-0a79baac6484', 'status': 'available', 'resource_id': '67d9726d-96f3-4088-8371-aeea62da6795', 'start_time': datetime(2020, 2, 29, 10, 30), 'end_time': datetime(2020, 3, 1, 10, 30), 'config': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 10}
offer1 = {'offer_id': '08d727a9-485a-4bf8-82e0-ee5f724e2020', 'project_id': '8057476a-1f6e-4749-9ebc-1989f7106c74', 'status': 'available', 'resource_id': '82ea2350-ff60-43f0-881f-3b7b9fdbd7c6', 'start_time': datetime(2020, 3, 1, 10, 30), 'end_time': datetime(2020, 3, 2, 10, 30), 'config': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 10}
offer2 = {'offer_id': '4b29b725-b20c-43c9-8d5e-c52ab8292ff3', 'project_id': '757a8472-b9eb-4143-ad50-5c5739157c29', 'status': 'available', 'resource_id': 'a1776463-664b-4cf2-ba8a-891870ead78d', 'start_time': datetime(2020, 3, 2, 10, 30), 'end_time': datetime(2020, 3, 3, 10, 30), 'config': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 10}
offer3 = {'offer_id': '32f51886-44c7-4df0-849c-95b25426a524', 'project_id': 'e1e32e48-8d98-4eca-8b69-3ef61f9f5848', 'status': 'available', 'resource_id': '8c127ab1-27d3-40f1-ac1b-09500156e0dc', 'start_time': datetime(2020, 3, 3, 10, 30), 'end_time': datetime(2020, 3, 4, 10, 30), 'config': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 10}
offer4 = {'offer_id': 'c4e9b878-61ee-4b07-9218-fa94c2bf6348', 'project_id': '30294371-e7bb-4c80-ab58-db4af239e33a', 'status': 'available', 'resource_id': 'e0c18d09-6275-4d12-a9f1-74df71fa09c3', 'start_time': datetime(2020, 3, 4, 10, 30), 'end_time': datetime(2020, 3, 5, 10, 30), 'config': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 10}
offer5 = {'offer_id': 'fa571588-7a9e-45d7-9a53-a869c00ce42a', 'project_id': '9ee3581b-9ea6-41d5-af19-da7bae4d555f', 'status': 'available', 'resource_id': '56d78001-f8d7-4a51-baee-3af6c685aebc', 'start_time': datetime(2020, 3, 5, 10, 30), 'end_time': datetime(2020, 3, 6, 10, 30), 'config': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 10}
offer6 = {'offer_id': '89b5de49-12c3-439b-be09-4e75454b94f4', 'project_id': 'cade37d2-a72b-49d2-a719-ad96ca89ae56', 'status': 'available', 'resource_id': 'cef6d2cb-cd28-45b3-97ed-59deb61a436a', 'start_time': datetime(2020, 3, 6, 10, 30), 'end_time': datetime(2020, 3, 7, 10, 30), 'config': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 10}
offer7 = {'offer_id': 'e185a350-5078-48fa-8488-584caa8e23fb', 'project_id': 'e8438d40-8a65-406d-8f9e-3812d6eadf12', 'status': 'available', 'resource_id': '59b397a0-f863-44a3-8ee7-59e4e3473c8a', 'start_time': datetime(2020, 3, 7, 10, 30), 'end_time': datetime(2020, 3, 8, 10, 30), 'config': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 10}
offer8 = {'offer_id': 'b235f398-368e-4059-b556-2bfbf15cf01f', 'project_id': '39ad89cc-ade2-40c4-a1ed-1375afdba763', 'status': 'available', 'resource_id': 'a2798b5d-8ec2-43a2-9e6f-297b8f9ed3ef', 'start_time': datetime(2020, 3, 8, 10, 30), 'end_time': datetime(2020, 3, 9, 10, 30), 'config': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 10}
offer9 = {'offer_id': '0921d243-3088-4662-9e9f-75087e4c18e7', 'project_id': '7e222bad-151d-41ce-a6ed-2138b047aa22', 'status': 'available', 'resource_id': 'e17d37c8-385a-47c3-9dd6-fbd168b81728', 'start_time': datetime(2020, 3, 9, 10, 30), 'end_time': datetime(2020, 3, 10, 10, 30), 'config': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 10}


bid0 = {'bid_id': '24ea1cc1-811f-437e-a748-b8a0f00cd401', 'project_id': 'ba0ee0fe-ee77-474e-8588-cf6a023c6c05', 'quantity': 1, 'start_time': datetime(2020, 2, 29, 10, 30), 'end_time': datetime(2020, 3, 1, 10, 30), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 11}
bid1 = {'bid_id': '6ee19822-d16e-4372-9f3d-5ae430237d30', 'project_id': '3b16fe2e-c59d-4cc5-a588-10a0603dc978', 'quantity': 1, 'start_time': datetime(2020, 3, 1, 10, 30), 'end_time': datetime(2020, 3, 2, 10, 30), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 11}
bid2 = {'bid_id': '45930fdb-e591-406e-98fc-56ab7a87db24', 'project_id': '526c62f1-b1f5-4c96-a7f2-a42de4616bc0', 'quantity': 1, 'start_time': datetime(2020, 3, 2, 10, 30), 'end_time': datetime(2020, 3, 3, 10, 30), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 11}
bid3 = {'bid_id': '9c713b4d-fddb-4e99-ae3e-5c02aadec389', 'project_id': '62d6266f-1596-4bf3-997d-e514907d4ec8', 'quantity': 1, 'start_time': datetime(2020, 3, 3, 10, 30), 'end_time': datetime(2020, 3, 4, 10, 30), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 11}
bid4 = {'bid_id': '2369d6ba-b841-4586-93c0-4d14571755ce', 'project_id': '488a1058-0e3a-4a8a-bded-33957058364f', 'quantity': 1, 'start_time': datetime(2020, 3, 4, 10, 30), 'end_time': datetime(2020, 3, 5, 10, 30), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 11}
bid5 = {'bid_id': '38ec7b78-d330-47d4-94f4-b5f904895cd3', 'project_id': '1f680a4a-d041-4533-814e-aed2e0ebbed5', 'quantity': 1, 'start_time': datetime(2020, 3, 5, 10, 30), 'end_time': datetime(2020, 3, 6, 10, 30), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 11}
bid6 = {'bid_id': '4cccbeaf-3e60-4dcc-8a3d-eba41e91c5a9', 'project_id': 'f1d75713-3815-4428-a7dd-085f737ad301', 'quantity': 1, 'start_time': datetime(2020, 3, 6, 10, 30), 'end_time': datetime(2020, 3, 7, 10, 30), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 11}
bid7 = {'bid_id': '9ae99e29-092d-492c-8f58-e804f1f21685', 'project_id': '9bdeeeb5-290a-48ed-a269-381ee3232f94', 'quantity': 1, 'start_time': datetime(2020, 3, 7, 10, 30), 'end_time': datetime(2020, 3, 8, 10, 30), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 11}
bid8 = {'bid_id': 'fcf1b70f-3236-41a5-bf65-be26e3ed8d56', 'project_id': '1857ca74-3690-4a5a-abf5-82ba5cd336a0', 'quantity': 1, 'start_time': datetime(2020, 3, 8, 10, 30), 'end_time': datetime(2020, 3, 9, 10, 30), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 11}
bid9 = {'bid_id': '0165c7d6-4e3d-4165-9c93-d423275a76bf', 'project_id': '45ab4988-8a5f-47e1-b3d1-7d86e984025f', 'quantity': 1, 'start_time': datetime(2020, 3, 9, 10, 30), 'end_time': datetime(2020, 3, 10, 10, 30), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 11}


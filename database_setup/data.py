import uuid
from datetime import datetime, timedelta
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

# provider_ids = []
# for i in range(0, 10):
#     provider_ids.append(uuid.uuid4())
#
# renter_ids = []
# for i in range(0, 10):
#     renter_ids.append(uuid.uuid4())

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


# config = {"memory_gb": 10240,
# "cpu_arch": "x86_64",
# "cpu_physical_count": 4,
# "cpu_core_count": 16,
# "cpu_ghz": 3
# }

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

# providers = []
# renters = []
# for i in range(0, 10):
#     providers.append(dict(user_id=provider_ids[i], username="provider" + str(i), role="provider", credit=100))
#     renters.append(dict(user_id=renter_ids[i], username="renter" + str(i), role="renter", credit=50))
#
#
# print(providers)
# print(renters)

offer0 = {'offer_id': '0ee67a67-f8e2-4db0-be81-fa9579f3ebd0', 'project_id': 'ab23f5d5-9718-4c8e-a499-0a79baac6484', 'status': 'available', 'resource_id': '67d9726d-96f3-4088-8371-aeea62da6795', 'start_time': datetime(2020, 5, 2, 8, 00), 'end_time': datetime(2020, 5, 2, 12, 00), 'expire_time': datetime(2020, 5, 1, 8, 00), 'config': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 10}
offer1 = {'offer_id': '08d727a9-485a-4bf8-82e0-ee5f724e2020', 'project_id': '8057476a-1f6e-4749-9ebc-1989f7106c74', 'status': 'available', 'resource_id': '82ea2350-ff60-43f0-881f-3b7b9fdbd7c6', 'start_time': datetime(2020, 5, 2, 10, 00), 'end_time': datetime(2020, 5, 2, 12, 00), 'expire_time': datetime(2020, 5, 1, 8, 00), 'config': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 20}
offer2 = {'offer_id': '4b29b725-b20c-43c9-8d5e-c52ab8292ff3', 'project_id': '757a8472-b9eb-4143-ad50-5c5739157c29', 'status': 'available', 'resource_id': 'a1776463-664b-4cf2-ba8a-891870ead78d', 'start_time': datetime(2020, 5, 2, 12, 00), 'end_time': datetime(2020, 5, 2, 14, 00), 'expire_time': datetime(2020, 5, 1, 8, 00), 'config': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 15}
offer3 = {'offer_id': '32f51886-44c7-4df0-849c-95b25426a524', 'project_id': 'e1e32e48-8d98-4eca-8b69-3ef61f9f5848', 'status': 'available', 'resource_id': '8c127ab1-27d3-40f1-ac1b-09500156e0dc', 'start_time': datetime(2020, 5, 2, 12, 00), 'end_time': datetime(2020, 5, 2, 16, 00), 'expire_time': datetime(2020, 5, 1, 8, 00), 'config': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 12}
offer4 = {'offer_id': 'c4e9b878-61ee-4b07-9218-fa94c2bf6348', 'project_id': '30294371-e7bb-4c80-ab58-db4af239e33a', 'status': 'available', 'resource_id': 'e0c18d09-6275-4d12-a9f1-74df71fa09c3', 'start_time': datetime(2020, 5, 2, 12, 00), 'end_time': datetime(2020, 5, 2, 18, 00), 'expire_time': datetime(2020, 5, 1, 8, 00), 'config': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 15}
offer5 = {'offer_id': 'fa571588-7a9e-45d7-9a53-a869c00ce42a', 'project_id': '9ee3581b-9ea6-41d5-af19-da7bae4d555f', 'status': 'available', 'resource_id': '56d78001-f8d7-4a51-baee-3af6c685aebc', 'start_time': datetime(2020, 5, 2, 14, 00), 'end_time': datetime(2020, 5, 2, 16, 00), 'expire_time': datetime(2020, 5, 1, 8, 00), 'config': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 17}
offer6 = {'offer_id': '89b5de49-12c3-439b-be09-4e75454b94f4', 'project_id': 'cade37d2-a72b-49d2-a719-ad96ca89ae56', 'status': 'available', 'resource_id': 'cef6d2cb-cd28-45b3-97ed-59deb61a436a', 'start_time': datetime(2020, 5, 2, 12, 00), 'end_time': datetime(2020, 5, 2, 16, 00), 'expire_time': datetime(2020, 5, 1, 8, 00), 'config': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 19}
offer7 = {'offer_id': 'e185a350-5078-48fa-8488-584caa8e23fb', 'project_id': 'e8438d40-8a65-406d-8f9e-3812d6eadf12', 'status': 'available', 'resource_id': '59b397a0-f863-44a3-8ee7-59e4e3473c8a', 'start_time': datetime(2020, 5, 2, 16, 00), 'end_time': datetime(2020, 5, 2, 20, 00), 'expire_time': datetime(2020, 5, 1, 8, 00), 'config': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 12}
offer8 = {'offer_id': 'b235f398-368e-4059-b556-2bfbf15cf01f', 'project_id': '39ad89cc-ade2-40c4-a1ed-1375afdba763', 'status': 'available', 'resource_id': 'a2798b5d-8ec2-43a2-9e6f-297b8f9ed3ef', 'start_time': datetime(2020, 5, 2, 20, 00), 'end_time': datetime(2020, 5, 2, 23, 00), 'expire_time': datetime(2020, 5, 1, 8, 00), 'config': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 15}
offer9 = {'offer_id': '0921d243-3088-4662-9e9f-75087e4c18e7', 'project_id': '7e222bad-151d-41ce-a6ed-2138b047aa22', 'status': 'available', 'resource_id': 'e17d37c8-385a-47c3-9dd6-fbd168b81728', 'start_time': datetime(2020, 5, 2, 20, 00), 'end_time': datetime(2020, 5, 2, 22, 00), 'expire_time': datetime(2020, 5, 1, 8, 00), 'config': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 17}


bid0 = {'bid_id': '24ea1cc1-811f-437e-a748-b8a0f00cd401', 'project_id': 'ba0ee0fe-ee77-474e-8588-cf6a023c6c05', 'quantity': 1, 'start_time': datetime(2020, 5, 2, 8, 00), 'end_time': datetime(2020, 5, 2, 12, 00), 'expire_time': datetime(2020, 5, 1, 1, 00), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 20}
bid1 = {'bid_id': '6ee19822-d16e-4372-9f3d-5ae430237d30', 'project_id': '3b16fe2e-c59d-4cc5-a588-10a0603dc978', 'quantity': 1, 'start_time': datetime(2020, 5, 2, 10, 00), 'end_time': datetime(2020, 5, 2, 12, 00), 'expire_time': datetime(2020, 5, 1, 2, 00), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 11}
bid2 = {'bid_id': '45930fdb-e591-406e-98fc-56ab7a87db24', 'project_id': '526c62f1-b1f5-4c96-a7f2-a42de4616bc0', 'quantity': 1, 'start_time': datetime(2020, 5, 2, 12, 00), 'end_time': datetime(2020, 5, 2, 14, 00), 'expire_time': datetime(2020, 5, 1, 3, 00), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 12}
bid3 = {'bid_id': '9c713b4d-fddb-4e99-ae3e-5c02aadec389', 'project_id': '62d6266f-1596-4bf3-997d-e514907d4ec8', 'quantity': 1, 'start_time': datetime(2020, 5, 2, 12, 00), 'end_time': datetime(2020, 5, 2, 16, 00), 'expire_time': datetime(2020, 5, 1, 4, 00), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 13}
bid4 = {'bid_id': '2369d6ba-b841-4586-93c0-4d14571755ce', 'project_id': '488a1058-0e3a-4a8a-bded-33957058364f', 'quantity': 1, 'start_time': datetime(2020, 5, 2, 12, 00), 'end_time': datetime(2020, 5, 2, 18, 00), 'expire_time': datetime(2020, 5, 1, 5, 00), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 14}
bid5 = {'bid_id': '38ec7b78-d330-47d4-94f4-b5f904895cd3', 'project_id': '1f680a4a-d041-4533-814e-aed2e0ebbed5', 'quantity': 1, 'start_time': datetime(2020, 5, 2, 14, 00), 'end_time': datetime(2020, 5, 2, 16, 00), 'expire_time': datetime(2020, 5, 1, 6, 00), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 15}
bid6 = {'bid_id': '4cccbeaf-3e60-4dcc-8a3d-eba41e91c5a9', 'project_id': 'f1d75713-3815-4428-a7dd-085f737ad301', 'quantity': 1, 'start_time': datetime(2020, 5, 2, 12, 00), 'end_time': datetime(2020, 5, 2, 16, 00), 'expire_time': datetime(2020, 5, 1, 7, 00), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 15}
bid7 = {'bid_id': '9ae99e29-092d-492c-8f58-e804f1f21685', 'project_id': '9bdeeeb5-290a-48ed-a269-381ee3232f94', 'quantity': 1, 'start_time': datetime(2020, 5, 2, 16, 00), 'end_time': datetime(2020, 5, 2, 20, 00), 'expire_time': datetime(2020, 5, 1, 8, 00), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 17}
bid8 = {'bid_id': 'fcf1b70f-3236-41a5-bf65-be26e3ed8d56', 'project_id': '1857ca74-3690-4a5a-abf5-82ba5cd336a0', 'quantity': 1, 'start_time': datetime(2020, 5, 2, 20, 00), 'end_time': datetime(2020, 5, 2, 23, 00), 'expire_time': datetime(2020, 5, 1, 9, 00), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 10}
bid9 = {'bid_id': '0165c7d6-4e3d-4165-9c93-d423275a76bf', 'project_id': '45ab4988-8a5f-47e1-b3d1-7d86e984025f', 'quantity': 1, 'start_time': datetime(2020, 5, 2, 20, 00), 'end_time': datetime(2020, 5, 2, 22, 00), 'expire_time': datetime(2020, 5, 1, 10, 00), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 10}

update_bid0 = {'bid_id': '24ea1cc1-811f-437e-a748-b8a0f00cd401', 'project_id': 'ba0ee0fe-ee77-474e-8588-cf6a023c6c05', 'quantity': 2, 'start_time': datetime(2020, 2, 29, 10, 30), 'end_time': datetime(2020, 3, 1, 10, 30), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 11}


provider0 = {'user_id': 'daf46548-eb35-4321-934d-36ed4e415d4b', 'username': 'provider0', 'role': 'provider', 'credit': 100}
provider1 = {'user_id': 'dd589ecb-ffbc-4a9c-a8d6-9db9cd3d7872', 'username': 'provider1', 'role': 'provider', 'credit': 100}
provider2 = {'user_id': 'afefd762-d4ff-430c-a350-09631c6bd30f', 'username': 'provider2', 'role': 'provider', 'credit': 100}
provider3 = {'user_id': '64587413-55d1-4b69-8560-fc2671599951', 'username': 'provider3', 'role': 'provider', 'credit': 100}
provider4 = {'user_id': 'dd711673-884c-46b2-8be6-ffc550ad0135', 'username': 'provider4', 'role': 'provider', 'credit': 100}
provider5 = {'user_id': 'd568eae2-a4f4-463a-a6d2-66effcdfb191', 'username': 'provider5', 'role': 'provider', 'credit': 100}
provider6 = {'user_id': '1ce58906-21e7-4f38-97d8-d9e7498fd070', 'username': 'provider6', 'role': 'provider', 'credit': 100}
provider7 = {'user_id': '16c4ef48-cd53-49b5-8b5f-3e98337f3023', 'username': 'provider7', 'role': 'provider', 'credit': 100}
provider8 = {'user_id': '2e13c3aa-711d-4bfe-a6aa-6dc8c37ae03d', 'username': 'provider8', 'role': 'provider', 'credit': 100}
provider9 = {'user_id': '4419671a-95e8-4544-93e1-ec7784fe9f75', 'username': 'provider9', 'role': 'provider', 'credit': 100}


renter0 = {'user_id': 'e7de4e71-163d-4627-934c-1b5db1348c0b', 'username': 'renter0', 'role': 'renter', 'credit': 50}
renter1 = {'user_id': 'cb3f37fc-d713-4728-98e7-4a2aeb398fab', 'username': 'renter1', 'role': 'renter', 'credit': 50}
renter2 = {'user_id': '4aaf82de-bc63-4867-9a23-9de257930d50', 'username': 'renter2', 'role': 'renter', 'credit': 50}
renter3 = {'user_id': 'f5bf81da-7cc7-44df-8484-a6eb2fa2d7e3', 'username': 'renter3', 'role': 'renter', 'credit': 50}
renter4 = {'user_id': 'eb69e81f-f203-4bd0-800d-6b20358428d3', 'username': 'renter4', 'role': 'renter', 'credit': 50}
renter5 = {'user_id': '64f4aab5-656a-4f87-9cc2-16f33a62b501', 'username': 'renter5', 'role': 'renter', 'credit': 50}
renter6 = {'user_id': '658c9564-a312-4ccc-afa2-e6f68c5975e2', 'username': 'renter6', 'role': 'renter', 'credit': 50}
renter7 = {'user_id': '92b73f4a-2228-499f-a19d-f14b45cd067b', 'username': 'renter7', 'role': 'renter', 'credit': 50}
renter8 = {'user_id': 'a7f88083-6b76-42cb-9b1c-3537d6f951c8', 'username': 'renter8', 'role': 'renter', 'credit': 50}
renter9 = {'user_id': 'b4156637-6b8d-47e8-b632-1c6838d2d663', 'username': 'renter9', 'role': 'renter', 'credit': 50}

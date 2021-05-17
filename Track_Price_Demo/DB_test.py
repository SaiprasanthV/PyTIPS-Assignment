import database
import time
from flask import Flask


###############################################################
# # adding user data - DONE

# print(database.add_user_data('Sai', 'sai@gmail.com', 123654896))
# print(database.add_user_data('Eswar', 'eswar@gmail.com', 125436845))
# print(database.add_user_data('Krishna', 'krishna@gmail.com', 957846654))
# print(database.add_user_data('Kumar', 'kumar@gmail.com', 4563858956))

# ###############################################################

# Testing User data

# print(database.get_user_id('sai@gmail.com'))

###############################################################

# # adding product data - DONE

# print(database.add_product_data('sai@gmail.com',
#       'Watch', '1H', 'sxchvgbhnjkkydgcfhvb', 1236))
# print(database.add_product_data('eswar@gmail.com',
#       'Laptop', '1D', 'djflkjfnlsjd', 56455))
# print(database.add_product_data(
#     'krishna@gmail.com', 'Mouse', '1H', 'woeitoidsndm', 846))
# print(database.add_product_data('sai@gmail.com',
#       'Mobile', '1H', 'sldjfnjsfof', 98412))
# print(database.add_product_data(
#     'eswar@gmail.com', 'Specs', '1D', 'wiuenfdjv', 5215))
# print(database.add_product_data(
#     'krishna@gmail.com', 'Charger', '1H', 'idbvifuvif', 852))
# print(database.add_product_data('sai@gmail.com',
#       'Ear Phone', '1D', 'owewflsjdnf', 3698))
# print(database.add_product_data(
#     'eswar@gmail.com', 'Dress', '1H', 'adfoirurod', 9874))
# print(database.add_product_data(
#     'kumar@gmail.com', 'Cable', '1H', 'aidnfiure', 1542))
# print(database.add_product_data('sai@gmail.com', 'Mask', '1H', 'ljdnfrhfu', 7853))
# print(database.add_product_data(
#     'eswar@gmail.com', 'Fan', '1H', 'skljdnfiurfn', 98523))
# print(database.add_product_data('kumar@gmail.com',
#       'TV', '1D', 'nvkrjheriuheinfh', 98741))

# ###############################################################

# Testing product data

# print(database.get_product_id('eswar@gmail.com', '1D', 'djflkjfnlsjd'))


# ###############################################################

# # adding track list data - DONE

# print(database.add_track_list_data(
#     'sai@gmail.com', '1H', 'sxchvgbhnjkkydgcfhvb', 65146))
# print(database.add_track_list_data(
#     'eswar@gmail.com', '1D', 'djflkjfnlsjd', 75345))
# print(database.add_track_list_data(
#     'krishna@gmail.com', '1H', 'woeitoidsndm', 543453))
# print(database.add_track_list_data('sai@gmail.com', '1H', 'sldjfnjsfof', 5656))
# print(database.add_track_list_data('eswar@gmail.com', '1D', 'wiuenfdjv', 4543))
# print(database.add_track_list_data('krishna@gmail.com', '1H', 'idbvifuvif', 456))
# print(database.add_track_list_data('sai@gmail.com', '1D', 'owewflsjdnf', 4564))
# print(database.add_track_list_data('eswar@gmail.com', '1H', 'adfoirurod', 23))
# print(database.add_track_list_data('kumar@gmail.com', '1H', 'aidnfiure', 865))
# print(database.add_track_list_data('sai@gmail.com', '1H', 'ljdnfrhfu', 348))
# print(database.add_track_list_data(
#     'eswar@gmail.com', '1H', 'skljdnfiurfn', 58783))
# print(database.add_track_list_data(
#     'kumar@gmail.com', '1D', 'nvkrjheriuheinfh', 98741))
# time.sleep(2)

# print(database.add_track_list_data(
#     'sai@gmail.com', '1H', 'sxchvgbhnjkkydgcfhvb', 65138))
# print(database.add_track_list_data('eswar@gmail.com', '1D', 'djflkjfnlsjd', 6843))
# print(database.add_track_list_data(
#     'krishna@gmail.com', '1H', 'woeitoidsndm', 8431))
# print(database.add_track_list_data('sai@gmail.com', '1H', 'sldjfnjsfof', 6948))
# print(database.add_track_list_data('eswar@gmail.com', '1D', 'wiuenfdjv', 5787))
# print(database.add_track_list_data('krishna@gmail.com', '1H', 'idbvifuvif', 8851))
# print(database.add_track_list_data('sai@gmail.com', '1D', 'owewflsjdnf', 6587))
# print(database.add_track_list_data('eswar@gmail.com', '1H', 'adfoirurod', 9874))
# print(database.add_track_list_data('kumar@gmail.com', '1H', 'aidnfiure', 6478))
# print(database.add_track_list_data('sai@gmail.com', '1H', 'ljdnfrhfu', 1541))
# print(database.add_track_list_data(
#     'eswar@gmail.com', '1H', 'skljdnfiurfn', 83147))
# print(database.add_track_list_data(
#     'kumar@gmail.com', '1D', 'nvkrjheriuheinfh', 8156))
# time.sleep(2)

# print(database.add_track_list_data(
#     'sai@gmail.com', '1H', 'sxchvgbhnjkkydgcfhvb', 96478))
# print(database.add_track_list_data(
#     'eswar@gmail.com', '1D', 'djflkjfnlsjd', 32154))
# print(database.add_track_list_data(
#     'krishna@gmail.com', '1H', 'woeitoidsndm', 6548))
# print(database.add_track_list_data('sai@gmail.com', '1H', 'sldjfnjsfof', 49326))
# print(database.add_track_list_data('eswar@gmail.com', '1D', 'wiuenfdjv', 4962))
# print(database.add_track_list_data('krishna@gmail.com', '1H', 'idbvifuvif', 3180))
# print(database.add_track_list_data('sai@gmail.com', '1D', 'owewflsjdnf', 62048))
# print(database.add_track_list_data('eswar@gmail.com', '1H', 'adfoirurod', 3045))
# print(database.add_track_list_data('kumar@gmail.com', '1H', 'aidnfiure', 30115))
# print(database.add_track_list_data('sai@gmail.com', '1H', 'ljdnfrhfu', 27853))
# print(database.add_track_list_data('eswar@gmail.com', '1H', 'skljdnfiurfn', 6244))
# print(database.add_track_list_data(
#     'kumar@gmail.com', '1D', 'nvkrjheriuheinfh', 55555))
# time.sleep(2)

# print(database.add_track_list_data(
#     'sai@gmail.com', '1H', 'sxchvgbhnjkkydgcfhvb', 86147))
# print(database.add_track_list_data('eswar@gmail.com', '1D', 'djflkjfnlsjd', 9614))
# print(database.add_track_list_data(
#     'krishna@gmail.com', '1H', 'woeitoidsndm', 6255))
# print(database.add_track_list_data('sai@gmail.com', '1H', 'sldjfnjsfof', 3254))
# print(database.add_track_list_data('eswar@gmail.com', '1D', 'wiuenfdjv', 6586))
# print(database.add_track_list_data(
#     'krishna@gmail.com', '1H', 'idbvifuvif', 85622))
# print(database.add_track_list_data('sai@gmail.com', '1D', 'owewflsjdnf', 9654))
# print(database.add_track_list_data('eswar@gmail.com', '1H', 'adfoirurod', 9644))
# print(database.add_track_list_data('kumar@gmail.com', '1H', 'aidnfiure', 1236))
# print(database.add_track_list_data('sai@gmail.com', '1H', 'ljdnfrhfu', 3412))
# print(database.add_track_list_data('eswar@gmail.com', '1H', 'skljdnfiurfn', 3215))
# print(database.add_track_list_data(
#     'kumar@gmail.com', '1D', 'nvkrjheriuheinfh', 9645))

###############################################################

# # delete product and track data of a product

# print(database.delete_product_data('sai@gmail.com', '1H', 'sxchvgbhnjkkydgcfhvb'))
# print(database.delete_product_data('krishna@gmail.com', '1H', 'idbvifuvif'))
# print(database.delete_product_data('eswar@gmail.com', '1H', 'skljdnfiurfn'))
# print(database.delete_product_data(
#     'kumar@gmail.com', '1D', 'nvkrjheriuheinfh'))


###############################################################

# # get all track data of a User - done

# print(database.show_all_track_data('sai@gmail.com'))

# print(database.show_all_track_data('eswar@gmail.com'))

# print(database.show_all_track_data('krishna@gmail.com'))

# print(database.show_all_track_data('kumar@gmail.com'))

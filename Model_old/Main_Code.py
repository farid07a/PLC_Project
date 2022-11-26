

class physical_plc:



    def __init__(self):
        print()

    def reading_data_from_physical_plc(self):
        def reading_data_from_physical_plc(self):
            print()
            while True:
                if plc.get_connected():
                    db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)
                    read_data_obj.Data_Input = db  # set dataBloc to DataInput to save with operation
                    read_data_obj.insert_input_data()  # save The operation read of data with primary key

                    list_tags = tag.list_of_tags()  # get list of tags to get id and
                    for tag_i in list_tags:

                        id_tag = tag_i.get_id_tag()
                        data_type = tag_i.get_data_type()
                        addres_byte = tag_i.get_address_start_byte()

                        print("ID_tag:", id_tag, "data_type:", data_type, "addres_byte:", addres_byte, "End_adres_byte",
                              addres_byte + 2)
                        part_of_tag = bytearray(4)

                        if data_type == "int":
                            part_of_tag = db[addres_byte:addres_byte + 2]
                            print("part of package from db :", part_of_tag)
                            print(get_int(db, addres_byte))

                        elif data_type == "real":
                            part_of_tag = db[addres_byte:addres_byte + 4]
                            print(get_int(db, addres_byte))

                        elif data_type == "bool":
                            addres_bit = tag_i.get_address_start_bit()
                            part_of_tag = db[addres_byte:addres_byte + 1]
                            print(snap7.util.get_bool(db, addres_byte, addres_bit))

                        id_read = read_data_obj.get_last_operation_read()  # return last id of Operation Read
                        print("Last ID of Operationread :", id_read)

                        split_data_tag.create(id_tag, id_read, part_of_tag)  #

                        split_data_tag.insert_split_data_package_database()  # insert data in database

                    sleep(1)
                else:
                    print("PLC no connected")
                    break






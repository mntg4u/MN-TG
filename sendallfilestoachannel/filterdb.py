async def horridfan():
    """Retrieve all file_ids from both Media and Media2 collections @HORRIDduo"""
    file_ids = []
    # dq primary database
    cursor1 = Media.find({})
    all_media1 = await cursor1.to_list(length=None)
    file_ids.extend(media.file_id for media in all_media1)
    # dq repo ayath kond second dbyum ang akki 
    cursor2 = Media2.find({})
    all_media2 = await cursor2.to_list(length=None)
    file_ids.extend(media.file_id for media in all_media2)
    return file_ids
def unpack_new_file_id(new_file_id):
    """Return file_id, file_ref"""
    decoded = FileId.decode(new_file_id)

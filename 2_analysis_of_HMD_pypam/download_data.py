import minio
import os
import pathlib

def download_data_station(station_name, client_obj, bucket_str, prefix_str, data_path, year):
    station_folder = pathlib.Path(data_path).joinpath(station_name)
    if not station_folder.exists():
        os.mkdir(station_folder)
    objects = list(client_obj.list_objects(bucket_str, prefix=prefix_str))
    ct = 0
    for i, obj in enumerate(objects):
        object_name = obj.object_name
        path_name = pathlib.Path(object_name).name
        if (not path_name.startswith('.')) & path_name.endswith('.nc'):
            if str(year) in path_name:
                download_path = data_path + '/' + station_name + '/' + pathlib.Path(object_name).name
                if os.path.isfile(download_path):
                    print('Already downloaded: ' + download_path)
                else:
                    print('Download ' + str(ct) + ' of ' + str(len(objects)) + ': ' + download_path)
                    object_data = client.get_object(bucket, object_name)
                    if not os.path.isdir(download_path):
                        with open(str(download_path), 'wb') as file_data:
                            for data in object_data:
                                file_data.write(data)
                    file_data.close()
            else: 
                print('Ignored: ' + path_name)
        ct += 1
    return ds3


if __name__ == '__main__':
    local_path = './data'
    # Set up the download for MARS data
    client = minio.Minio( "s3.us-west-2.amazonaws.com", secure=False)
    
    bucket = 'pacific-sound-spectra'
    prefix = '2021/'
    station = 'MARS'
    ss = download_data_station(station, client, bucket, prefix, local_path, year=2021)

    # Set up the download for NRS11 data 
    client = minio.Minio('storage.googleapis.com')
    bucket = 'noaa-passive-bioacoustic'
    station = 'NRS11'
    prefix = 'soundcoop/%s/' % station
    download_data_station(station, client, bucket, prefix, local_path, year=2021)

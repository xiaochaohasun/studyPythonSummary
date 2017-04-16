#!/usr/bin/env python

import cPickle as p
import hashlib
import os
import tarfile
import time




def check_md5(filename):
    m=hashlib.md5()
    with open(filename) as fobj:
        while True:
            data=fobj.read(4096)
            if data == '':
                break
            m.update(data)
    return m.hexdigest()


def full_backup(src_dir,dst_dir,md5_file):
    md5_dict={}
    backup_name='%s_full_%s.tar.gz' % \
                (
                    os.path.basename(src_dir.rstrip('/')),
                    time.strftime('%Y%m%d')
                )
    full_backupname=os.path.join(dst_dir,backup_name)
    tar=tarfile.open(full_backupname,'w:gz')
    tar.add(src_dir)
    tar.close()

    for path,folder,files in os.walk(src_dir):
        for each_file in files:
            abs_path=os.path.join(path,each_file)
            md5_dict[abs_path]=check_md5(abs_path)

    with open(md5_file,'w') as fobj:
        p.dump(md5_dict,fobj)



def incr_backup(src_dir,dst_dir,md5_file):
    new_md5_dict={}
    backup_name='%s_incr_%s.tar.gz' % \
                (
                    os.path.basename(src_dir.rstrip('/')),
                    time.strftime('%Y%m%d')
                )
    incr_backupname=os.path.join(dst_dir,backup_name)

    with open(md5_file) as fobj:
        old_md5=p.load(fobj)

    for path,folder,files in os.walk(src_dir):
        for each_file in files:
            abs_path=os.path.join(path,each_file)
            new_md5_dict[abs_path]=check_md5(abs_path)

    with open(md5_file,'w') as fobj:
        p.dump(new_md5_dict,fobj)

    tar=tarfile.open(incr_backupname,'w:gz')
    for key in new_md5_dict:
        if new_md5_dict[key] != old_md5.get(key):
            tar.add(key)
    tar.close()


if __name__ == '__main__':
    src_dir='/usr/local/ebook/'
    dst_dir='/tmp/backup/'
    md5_file='/tmp/backup/md5.data'
    if not os.path.isdir(dst_dir):
        os.mkdir(dst_dir)
    # full_backup(src_dir,dst_dir,md5_file)
    incr_backup(src_dir,dst_dir,md5_file)
    # if time.strftime('%a') == 'Mon':
    #     full_backup(src_dir,dst_dir,md5_file)
    # else:
    #     incr_backup(src_dir,dst_dir,md5_file)
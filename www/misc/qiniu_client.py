# -*- coding: utf-8 -*-


"""
@attention: 七牛客户端
@author: lizheng
@date: 2014-03-15
"""

from django.conf import settings
import StringIO
import logging
import json
import qiniu.io
import qiniu.rs

from common import utils


HASH_KEY = 'zhixuanimg20140315'
AK = 'DdZbYWvnh7XAEnu9s4WqnbN-7_0qM23lcKitiKrx'
SK = '1VU-ve9ecmMDFBRvI-pWxTsW4oq4uS-c1Ea5WuxP'

qiniu.conf.ACCESS_KEY = AK
qiniu.conf.SECRET_KEY = SK


def get_upload_token(img_key=None, img_type='avatar', scope='zimg0'):
    if img_key:
        scope = '%s:%s' % (scope, img_key)
    if img_type == 'avatar':
        returnUrl = '%s/qiniu_img_return' % settings.MAIN_DOMAIN
    else:
        returnUrl = ''
    returnBody = ('{"user_id":$(x:user_id), "img_type":$(x:img_type), "key":$(key),  "hash":$(etag), "w":$(imageInfo.width), '
                  '"h":$(imageInfo.height), "bucket":$(bucket)}')

    policy = qiniu.rs.PutPolicy(scope=scope)
    if returnUrl:
        policy.returnUrl = returnUrl
    policy.returnBody = returnBody
    policy.insertOnly = 1
    uptoken = policy.token()
    return uptoken


def upload_img(file_data, img_type='editor'):
    # extra = qiniu.io.PutExtra()
    # extra.mime_type = "image/jpeg"

    # data 可以是str或read()able对象
    data = StringIO.StringIO(file_data.read())
    uptoken = get_upload_token(img_type=img_type)
    key = '%s_%s' % (img_type, utils.uuid_without_dash())
    ret, err = qiniu.io.put(uptoken, key, data)
    # print ret, err
    if err is not None:
        logging.error('upload_img error is:%s' % err)
        return False, err

    key = ret.get('key', '')
    # 编辑器上传图片最大宽度为600
    if img_type == 'editor':
        if int(ret.get('w', 0)) > 600:
            key += '!600m0'
    return True, key

if __name__ == '__main__':
    get_upload_token()

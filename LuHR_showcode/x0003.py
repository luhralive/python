#将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
import redis
import x0001

redisHost = '192.168.100.123'
redisPort = 6379

def storeRedis(codelist):
    r = redis.StrictRedis(host=redisHost, port=redisPort)
    for i in range(len(codelist)):
        r.set('key_'+ str(i), codelist[i - 1])

def searchRedis():
    r = redis.StrictRedis(host=redisHost, port=redisPort,db=0)
    b = int(input('Search Active code（1-200）：'))
    value = r.get('key_' + str(b))
    print(value)



if __name__ == '__main__':
    codelist = x0001.get_ACCode(20,5)
    storeRedis(codelist)
    searchRedis()

# Question
---

At Ormuco, we want to optimize every bits of software we write. Your goal is to write a new library that can be integrated to the Ormuco stack. Dealing with network issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria:

    1 - Simplicity. Integration needs to be dead simple.
    2 - Resilient to network failures or crashes.
    3 - Near real time replication of data across Geolocation. Writes need to be in real time.
    4 - Data consistency across regions
    5 - Locality of reference, data should almost always be available from the closest region
    6 - Flexible Schema
    7 - Cache can expire

---

# Resolution

I achieved to implement a full lru for any key, value pair. it is easy to integrate with a simple decorator to apply on already existent function used to access key, value pair.

``` python
import lru
a = lru.LRUModule(cacheSize=2)
nonCached = {1:1,2:2,3:3,4:4,5:5,6:6,7:7}

@a.accessDecorator
def get(key):
    return nonCached[key]

@a.writeDecorator
def write(key, value):
    nonCached[key] = value

get(1)==1 # This will use the cached version if already cached otherwise it will cache it
write(8, "s") # this will edit both the cached version and nonCached version
```

To achieve *Near real time replication of data across Geolocation.* I've used websocket connection and pickle.
You first need to run a brocker which will transmit data to every client in real time.
```
python broker.py
```
This will start a infinite loop server on port 5010.

Then, you need to open client on multiple location. For this i'm using python terminal.
``` python
import dt
import lru
host = "localhost"
a = lru.LRUModule(cacheSize = 5)
nonCached = {}
d = dt.dataTrans(host, 5010)
@ d.editDecorator
@ a.writeDecorator
def write(key, value):
   nonCached[key] = value

```
change `host` accordingly

then try to use the write function changes will be replicated over all the client in real time
```python
write("test","a")
```

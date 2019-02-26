Software Engineering Trends on Docker Hub
=========================================


# Expectations

1. Play with the following APIs : 


    1. `https://hub.docker.com/api/content/v1/products/search?page_size=<x>&q=&type=image` 
    (example : https://hub.docker.com/api/content/v1/products/search?page_size=25&q=&type=image&page=3  
    You may check out hub.docker.com and view API traffic via the chrome developer console). Understand how you could write scripts to call Hub and get the data you want with respect to all repositories that are surfaced via this API.
    2. `https://hub.docker.com/v2/repositories/<namespace>/<name>/` 
    (example : https://hub.docker.com/v2/repositories/library/busybox/)
    this surfaces all details about a repository that is publicly available, except Dockerfile.

    3. Obtain Dockerfile in addition: 
  NOTE: this is only available for a subset of repositories, and can be additional information that can be surfaced. `https://hub.docker.com/v2/repositories/<namespace>/<name>/dockerfile/ `(Example: https://hub.docker.com/v2/repositories/swce/keyval-resource/dockerfile/) 

2. Add scripts to read through the APIs.
   Note : Add timeouts between calls you make to hub, (1 second sleep)
   .If you make too many calls, you might get blocked. 

3. Inference #1 : 
   Based on data collected in (2), what kind of repositories were popular per month since June 2014 (look at create time on these repositories to infer popularity).

4. Inference #2 : 
   What was the velocity of new content (new repositories that were created) vs duplicated content (people pushing content from other people). 

5. Inference #3 :
     What were popular images by pulls (note that 3 is popular images in terms of number of images created). 

Beyond point 5, I'd ask for the following general inferences.

1. Kinds of content popular at any given point (standalone images, what kind? Applications or collections of images, what kind?)
2. Are you able to correlate this with general industry trends at any given point in time. 
3. What do you think users will gravitate to in the future.
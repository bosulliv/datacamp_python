# Readme
This was a really interesting course.

### pipe.predict() from pick encapsulation
For mature models, with a small number of transformations, Pipelines are a clean way to deliver production estimators. In particular, having the pipe.predict() include all the feature transformations, is a nice encapsulation.

But I hesitate to use Pipelines for less mature models, or ones with lots of features and transformations - for instance, my customer retention model would be very hard to understand and troubleshoot if built as a Pipeline object. I think the decomposition of sub-classes in the feature cleaning and transformation makes it much easier for another data scientist to pick up my code, understand it, and either tweak existing features, or add new ones. The same process as a Pipeline feels like it would need to be first unpacked, reconsidered, then repacked into a pipeline call: That's a lot for somebody to hold in their head.

I'm also hesitant to perform model fitting automatically - it is so important to run the fine tooth comb over the predictions: And whilst you can automate some sense checks - those will not pick up biases or decide to transform features which have a weak linear signature.

That analysis benefits from human creativity, especially when motivated by the fear of producing highly 'accurate' results, which are not always the same as highly useful results: This is particularly the case when there is a strong bias in the trained data, which is not present in reality.

### Dataset Shift
Sometimes we set arbitrary windows for temporal data - these should be tested with window size which slides over our dataset. Of course, in this instance seasonality needs to be balanced with recency. With something as complicated as customer retention, I would bias towards recency, rather than long measures of seasonality - or indeed, split models into customers where seasonality is an important predictor, whereas newer or more changeable customers benefit from models of recent data.

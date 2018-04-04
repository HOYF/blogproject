# -*- conding:utf-8 -*-

# 带高亮搜索功能实现

# 说明：要相对某个 app 下的数据进行全文检索，就要在该 app 下创建一个 search_indexes.py 文件，
# 然后创建一个 XXIndex类（XX为含有被检索数据的模型，如这里的Post）,并且继承 SearchIndex 和 Indexable

from haystack import indexes
from .models import Post

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    # 每个索引里面必须有且只能有一个字段为 document=True ，这代表 django haystack 和 搜索引擎将使用此字段的内容作为索引进行检索
    # 注意：如果使用一个字段设置了 document=True ，则一般约定此字段名为text，这是在 SearchIndex 类里面一贯的命名，以防止后台混乱，当然名字你也可以随便改，不过不建议改
    # haystack 提供了 use_template=True 在 text 字段中，这样就允许我们使用数据模板去简历搜索引擎索引的文件，说得通俗点就是索引里面存放一些什么东西，例如Post 的 title 字段，
    # 这样我们可以通过 title 内容来检索 Post 数据来。
    # 举个例子：加入你搜索 Python ，那么就可以检索出 title 中含有 Python 的 Post 了。
    # 数据模板的路径为 templates/search/indexes/youapp/\<model_name>_text.txt（例如 templates/search/indexes/blog/post_text.txt）
    text = indexes.CharField(document=True, use_template=True)
    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

# 为什么要创建索引？索引就像是一本书的目录，可以为读者提供更快速的导航与查找。
# 在这里也是同样的道理，当数据量非常大的时候，若要从这些数据里找出所有的满足搜索条件的几乎是不太可能的，将会给服务器带来极大的负担。
# 所以我们需要为指定的数据添加一个索引（目录），在这里是为 Post 创建一个索引，索引的实现细节是我们不需要关心的，我们只关心为哪些字段创建索引，如何指定。
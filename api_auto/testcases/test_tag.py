import pytest

from api_auto.api.tag import Tag


class TestTag:
    def setup_class(self):
        self.tag=Tag()

    def test_get(self):
        assert self.tag.get()["errmsg"]== "ok"
    # 准备测试数据userid、name、mobile
    create_data = [('tagname' + str(x), x) for x in range(10,20)]
    @pytest.fixture(scope="module")
    def taginfo(self,request):
        data=request.param
        return data

    @pytest.mark.parametrize("tagname,tagid", [("good6", 6), ("bad7", 7)])
    def test_update(self,tagname,tagid):
        self.tag.update(tagname,tagid)

    @pytest.mark.parametrize("taginfo", create_data)
    def test_create(self,taginfo):
        self.taglist=self.tag.get()["taglist"]
        print(self.taglist)
        self.flag=True
        for index in range(0,len(self.taglist)):
            if taginfo[1] == self.taglist[index]["tagid"]:
                print("aready exit tag")
                self.flag=False
                break
        if self.flag:
            assert self.tag.create(*taginfo)[ "errmsg"]=="created"
            print(self.tag.get())
            assert self.tag.delete(taginfo[1])[ "errmsg"]=="deleted"




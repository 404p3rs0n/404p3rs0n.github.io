# LoveIt主题博客搭建指北


## 博客搭建

brew一键安装hugo

```bash
brew install hugo
hugo version
```

安装之后创建博客站点

```bash
hugo new site 404p3rs0n
```

![image-20230819171416735](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230819171416735.png)

创建后下载主题放到themes文件夹下，在hugo.toml中添加主题

![image-20230819171457600](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230819171457600.png)

或直接指定参数在本地进行测试

```bash
hugo server -t LoveIt --buildDrafts
```

配置成功后，上传github仓库，如果出现鉴权失败

> 注：创建的Github仓库需要以username.github.io格式命名，且仓库属性为Public。

![image-20230819222218952](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230819222218952.png)

在github中setting中找到Developer setting创建tokens，然后在push的时候输入密码时输入token就可以了

![image-20230819222400361](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230819222400361.png)

上传到github仓库后，如下图进行Deploy之后Github-pages功能即可使用

![image-20230820142540778](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230820142540778.png)

部署完成之后将仓库拉取到本地进行同步，以免丢失.github文件夹中的内容导致文章上传之后不能更新的问题

```bash
git pull origin master
```

![image-20230821200147884](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230821200147884.png)

在进行上传之后会自动执行Actions

![image-20230821200505445](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230821200505445.png)

## 图床设置

在Github上新建一个Public属性的仓库用来存放图片

![image-20230821092716285](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230821092716285.png)

用之前生成的Token配置PicGo访问Github上传图片

![image-20230821093551523](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230821093551523.png)

配置成功之后即可上传图片至Github仓库

> 这里还是建议使用图床对图片进行保存，不影响图片加载速度和图片安全性。

## 一键上传

> 苦于一次次执行git，才有了这个脚本，python执行即可

```python
python GitPush.py
```

![image-20230821200318143](https://21r000-image.oss-cn-shanghai.aliyuncs.com/2023/image-20230821200318143.png)

## Posts实现md5加密

> 苦于文章Title为中文时，Posts经url转换后会很长，于是自定义slug为Title的md5值

修改文章模版 `archetypes/default.md`，在Front-matter中添加slug字段，新建文章时将文章创建时间和标题进行md5加密，从第0位取到第16位作为slug

```bash
slug: {{ substr (md5 (printf "%s%s" .Date (replace .TranslationBaseName "-" " " | title))) 0 16 }}
```

在网站配置 `hugo.toml` 中添加文章永久链接选项

```toml
permalinks:
  posts = ":year/:month/:slug"
```

## 图片表格居中

根据自定义样式规则，在网站根目录下创建 `assets/css/_custom.css`，代码如下：

```css
.post-content img {
    margin-left: auto;
    margin-right: auto;
}

.post-content table {
  	/* 列宽自适应 */
    width: fit-content; 
    display: table;
    margin-left: auto;
    margin-right: auto;
}
```



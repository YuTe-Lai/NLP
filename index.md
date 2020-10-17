## 資料預處理：讓機器能夠吸收文字

### Step 1.文本斷詞（Text Segmentation）
將文本切割成數個有意義的單位（Character、Word、Sentence），而切割完成後的每個文字片段習慣被稱為Token。

．英文可以簡單地用空格斷詞：
```markdown
text = 'I am a student major in data science.'
words = text.split(' ')
```

．中文則使用 Jieba 中文斷詞工具：
```markdown
import jieba.posseg as pseg

text = '我是主修資料科學的學生'
words = pseg.cut(text)
[word for word in words]

#標點符號的 flag == x ，如果要去除標點符號可以補上`flag in words if flag != 'x'`。
```

### Step 2.將文本轉成數字序列
### Step 3.整合序列長度（Zero Padding）
### Step 4.將正解做 One-hot Encoding


### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/YuTe-Lai/NLP/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.

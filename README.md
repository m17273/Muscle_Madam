# Muscle_Madam

## REST API 사용법 🧚

<br>

### Swagger UI

![Fast API docs](docs/images/fast_api.png)

#### API 리스트
- `Menus`
- `Comments`
- `Restaurants`

#### 스키마 리스트
- `Comment`
- `CommentRequest`
- `Menu`
- `MenuRequest`
- `Restaurant`
- `RestaurantRequest`


<br>

<hr>

<br>

## **API 별 사용법** 📝
<br>

### **Comments API**
<br>

1. **에디터 별 코멘트 조회** (success: 200 / fail: 404)

    status code 404의 경우 해당하는 에디터의 코멘트 없음

```javascript
/comments/editors/{editor_id}
```

`사용예제`
```javascript
$.ajax({
    url: "/comments/editors/1",
    type: "GET",
    ...
})
```

<hr>
<br>

2. **메뉴 별 코멘트 조회** (success: 200 / fail: 404)

    status code 404의 경우 해당 메뉴의 코멘트 없음

```javascript
/comments/menus/{menu_id}
```

`사용예제`
```javascript
$.ajax({
    url: "/comments/menus/1",
    type: "GET",
    ...
})
```

<hr>
<br>

3. **코멘트 생성** (success: 201 / fail: 409)

    status code 409의 경우, 이미 해당 메뉴에 해당 에디터가 작성한 코멘트가 존재함.
    (1인당 메뉴마다 코멘트 하나로 제한)

```javascript
/comments/
```

`사용예제`
```javascript
$.ajax({
    url: "/comments/",
    type: "POST",
    ...
})
```

<hr>
<br>

4. **코멘트 업데이트** (success: 200 / fail: 404)

    status code 404의 경우, comment_id에 해당하는 코멘트가 존재하지 않음.

```javascript
/comments/{comment_id}
```

`사용예제`
```javascript
$.ajax({
    url: "/comments/1",
    type: "PUT",
    ...
})
```


<hr>
<br>

4. **코멘트 삭제** (success: 204 / fail: 404)

    status code 404의 경우, comment_id에 해당하는 코멘트가 존재하지 않음.

```javascript
/comments/{comment_id}
```

`사용예제`
```javascript
$.ajax({
    url: "/comments/1",
    type: "DELETE",
    ...
})
```
function njulogin() {
    $url = "http://p.nju.edu.cn/portal_io/login"

    # edit username and password here
    $value = @{ username=""; password="" }
    $webRes = Invoke-WebRequest -UseBasicParsing -Uri $url -Method POST -Body $value
    
    $res = ConvertFrom-Json $webRes.Content
    
    if ($res.reply_code -eq 3) {
        "登录错误"
        ""
        $res
    } else {
        $res.reply_msg
        ""
        "用户名：" + $res.userinfo.username
        "姓名：" + $res.userinfo.fullname
        "区域：" + $res.userinfo.area_name
        "余额：" + $res.userinfo.balance
    }
}

njulogin

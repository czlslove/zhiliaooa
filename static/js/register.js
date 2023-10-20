//在网页加载完成后在执行以下函数
function bindEmail(){
    $("#captcha-btn").click(function (event){
        let $this=$(this)
        event.preventDefault();

        var email = $("input[name='email']").val()

        $.ajax({
            url:"/auth/captcha/email?email="+email,
            method:"GET",
            success:function(result){
                var code =result['code']
                if (code == 200){
                    let countdown=5
                    $this.off("click")
                    let timer=setInterval(function (){
                        $this.text(countdown)
                        countdown-=1
                        if(countdown<=0){
                            clearInterval(timer)
                            $this.text("获取验证码")
                            bindEmail()
                        }
                    },1000)
                    // alert("验证码发送成功！")
                }else{
                    alert(result['message'])
                }
            },
            fail:function(error){
                console.log(error)
            }
        })
        // alert(email)
    })
}

$(function(){
    bindEmail()
})
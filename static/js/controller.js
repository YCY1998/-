       
function get_time(){

$.ajax({
    url:'/time',
    timeout:100000,
    success:function(data){
        $("#tim").html(data)

    },
    error:function(xhr,type,errorThrown){

    }

}
);

}
function get_data(){
$.ajax({ 
    url:'/data',
    timeout: 100000,
    success:function(data){
        $(".num h1").eq(0).text(data.confirm);
        $(".num h1").eq(1).text(data.suspect);
        $(".num h1").eq(2).text(data.heal);
        $(".num h1").eq(3).text(data.dead);
    },
    error:function(xhr,type,errorThrown){

    }

});
}
function get_c2(){
    $.ajax({ 
        url:'/c2',
        timeout: 100000,
        success:function(data){
            ec_center_option.series[0].data=data.data;
            ec_center.setOption(ec_center_option);
        },
        error:function(xhr,type,errorThrown){
    
        }
    
    });
    }
function get_l1(){
    $.ajax({ 
        url:'/l1',
        timeout: 100000,
        success:function(data){
            ec_left1_Option.xAxis[0].data=data.data[0];
            ec_left1_Option.series[0].data=data.data[1];
            ec_left1_Option.series[1].data=data.data[2];
            ec_left1_Option.series[2].data=data.data[3];
            ec_left1_Option.series[3].data=data.data[4];
            ec_left1.setOption(ec_left1_Option);
        },
        error:function(xhr,type,errorThrown){
    
        }
    
    });
    }
function get_l2(){
    $.ajax({ 
        url:'/l2',
        timeout: 100000,
        success:function(data){
            ec_left2_Option.xAxis[0].data=data.data[0];
            ec_left2_Option.series[0].data=data.data[1];
            ec_left2_Option.series[1].data=data.data[2];
            ec_left2.setOption(ec_left2_Option);
        },
        error:function(xhr,type,errorThrown){
    
        }
    
    });
    }
function get_r1(){
    $.ajax({ 
        url:'/r1',
        timeout: 100000,
        success:function(data){
            ec_right1_option.xAxis.data=data.data[0];
            ec_right1_option.series[0].data=data.data[1];
            ec_right1.setOption(ec_right1_option);
        },
        error:function(xhr,type,errorThrown){
    
        }
    
    });
    }
function get_r2(){
    $.ajax({ 
        url:'/r2',
        timeout: 100000,
        success:function(data){
            ec_right2_option.series[0].data=data.data;
            ec_right2.setOption(ec_right2_option);
        },
        error:function(xhr,type,errorThrown){
    
        }
    
    });
    }
get_time()
get_data()
get_c2()
get_l1()
get_l2()
get_r1()
get_r2()
setInterval(get_time,1000)
setInterval(get_data,1000*3600)
setInterval(get_c2,1000*3600*24)
setInterval(get_l1,1000*3600*24)
setInterval(get_l2,1000*3600*24)
setInterval(get_r1,1000*3600*24)
setInterval(get_r2,1000*3600*12)
             
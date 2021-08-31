function calculateHeadcount() {

    let vehicle_total = 0;
    let headcount_total = 0;

    let vehicle_agency = {
        '원주소방서' : 0,
        '응원소방서' : 0,
        '타시도' : 0,
        '유관기관' : 0
    }

    let headcount_agency = {
        '원주소방서' : 0,
        '응원소방서' : 0,
        '타시도' : 0,
        '유관기관' : 0
    }

    let vehicle_dict = {
        '펌프' : '펌프',
        '물탱크' : '물탱크',
        '지휘' : '기타',
        '경형사다리차' : '기타',
        '고가사다리차' : '기타',
        '굴절차' : '기타',
        '화학차' : '화학차',
        '구급' : '구급',
        '구조공작' : '구조',
        '수난구조' : '구조',
        '산악구조' : '구조',
        '생활안전' : '구조',
        '배연차' : '기타',
        '화물차' : '기타',
        '버스' : '기타',
        '무인방수차' : '기타',
        '유관기관펌프' : '펌프',
        '유관기관물탱크' : '물탱크',
        '굴삭기' : '기타' ,
        '순찰차' : '기타' ,
        '행정차' : '기타',
        '작업차' : '기타',
        '기타' : '기타'
    }

    let vehicle_vehicle = {
        '펌프' : 0,
        '물탱크' : 0,
        '화학차' : 0,
        '구급' : 0,
        '구조' : 0,
        '기타' : 0
    }

    let headcount_vehicle = {
        '펌프' : 0,
        '물탱크' : 0,
        '화학차' : 0,
        '구급' : 0,
        '구조' : 0,
        '기타' : 0
    }

    Array.from(document.getElementById('dispatchedTeam-table').rows).slice(1).forEach(function (x) {
        let dispatchedTeam = x.getElementsByTagName('td');

        if(dispatchedTeam[4].getElementsByTagName('input')[0].checked) {
            let agency = dispatchedTeam[0].innerText;
            let vehicle = dispatchedTeam[2].innerText;
            let headcount = parseInt(dispatchedTeam[3].getElementsByTagName('input')[0].value);

            vehicle_total += 1;
            headcount_total += headcount;

            vehicle_agency[agency] += 1;
            headcount_agency[agency] += headcount;

            vehicle_vehicle[vehicle_dict[vehicle]] += 1;
            headcount_vehicle[vehicle_dict[vehicle]] += headcount;
        }
    })
    
    document.getElementById('vehicle-wonju').innerHTML = vehicle_agency['원주소방서'];
    document.getElementById('vehicle-support').innerHTML = vehicle_agency['응원소방서'];
    document.getElementById('vehicle-other').innerHTML = vehicle_agency['타시도'];
    document.getElementById('vehicle-coorperated').innerHTML = vehicle_agency['유관기관'];
    document.getElementById('vehicle-total').innerHTML = vehicle_total;

    document.getElementById('headcount-wonju').innerHTML = headcount_agency['원주소방서'];
    document.getElementById('headcount-support').innerHTML = headcount_agency['응원소방서'];
    document.getElementById('headcount-other').innerHTML = headcount_agency['타시도'];
    document.getElementById('headcount-coorperated').innerHTML = headcount_agency['유관기관'];
    document.getElementById('headcount-total').innerHTML = headcount_total;

    document.getElementById('vehicle-pump').innerHTML = vehicle_vehicle['펌프'];
    document.getElementById('vehicle-tank').innerHTML = vehicle_vehicle['물탱크'];
    document.getElementById('vehicle-chemical').innerHTML = vehicle_vehicle['화학차'];
    document.getElementById('vehicle-ambulance').innerHTML = vehicle_vehicle['구급'];
    document.getElementById('vehicle-rescue').innerHTML = vehicle_vehicle['구조'];
    document.getElementById('vehicle-etc').innerHTML = vehicle_vehicle['기타'];

    document.getElementById('headcount-pump').innerHTML = headcount_vehicle['펌프'];
    document.getElementById('headcount-tank').innerHTML = headcount_vehicle['물탱크'];
    document.getElementById('headcount-chemical').innerHTML = headcount_vehicle['화학차'];
    document.getElementById('headcount-ambulance').innerHTML = headcount_vehicle['구급'];
    document.getElementById('headcount-rescue').innerHTML = headcount_vehicle['구조'];
    document.getElementById('headcount-etc').innerHTML = headcount_vehicle['기타'];
}


if (document.getElementById('dispatchedTeam-table')) {
    calculateHeadcount();
}

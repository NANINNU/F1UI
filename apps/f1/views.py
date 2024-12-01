from django.shortcuts import render
from .models import Drivers, Constructors, Races, Results

def f1_search(request):
    search_type = request.GET.get('search_type', '')  # driver 또는 constructor
    query = request.GET.get('query', '')  # 검색어
    circuit_query = request.GET.get('circuit', '')  # 서킷 이름

    suggestions = []  # 자동완성용 이름 목록
    circuits = None
    graph_labels = []
    graph_data = []

    if search_type == 'driver':
        # 드라이버 이름 검색
        suggestions = Drivers.objects.filter(name__icontains=query)
        if query and len(suggestions) == 1:  # 정확한 드라이버 선택 시
            driver = suggestions.first()

            # 드라이버가 출전한 레이스 ID 가져오기
            race_ids = Results.objects.filter(driverid=driver.driverid).values_list('raceid', flat=True)

            # 드라이버가 출전한 서킷 목록 가져오기
            circuits = Races.objects.filter(raceid__in=race_ids).values('name').distinct()

            # 선택된 서킷으로 그래프 데이터 생성
            if circuit_query:
                # 선택된 서킷의 레이스 데이터 가져오기
                selected_races = Races.objects.filter(name=circuit_query, raceid__in=race_ids).values('raceid', 'year')

                # 선택된 서킷의 Results에서 데이터 가져오기
                results = Results.objects.filter(
                    raceid__in=[race['raceid'] for race in selected_races],
                    driverid=driver.driverid
                ).values('raceid', 'position')

                # 그래프 데이터 생성
                year_position_map = {race['year']: None for race in selected_races}  # 초기화

                for result in results:
                    for race in selected_races:
                        if result['raceid'] == race['raceid']:
                            year_position_map[race['year']] = result['position']
                            break

                # 그래프용 라벨 및 데이터 생성 (출전한 연도만 포함)
                graph_labels = sorted([year for year, position in year_position_map.items() if position is not None])
                graph_data = [year_position_map[year] for year in graph_labels]

    elif search_type == 'constructor':
        # 컨스트럭터 이름 검색
        suggestions = Constructors.objects.filter(name__icontains=query)
        if query and len(suggestions) == 1:  # 정확한 컨스트럭터 선택 시
            constructor = suggestions.first()

            # 컨스트럭터가 출전한 레이스 ID 가져오기
            race_ids = Results.objects.filter(constructorid=constructor.constructorid).values_list('raceid', flat=True)

            # 컨스트럭터가 출전한 서킷 목록 가져오기
            circuits = Races.objects.filter(raceid__in=race_ids).values('name').distinct()

            # 선택된 서킷으로 그래프 데이터 생성
            if circuit_query:
                # 선택된 서킷의 레이스 데이터 가져오기
                selected_races = Races.objects.filter(name=circuit_query, raceid__in=race_ids).values('raceid', 'year')

                # 선택된 서킷의 Results에서 데이터 가져오기
                results = Results.objects.filter(
                    raceid__in=[race['raceid'] for race in selected_races],
                    constructorid=constructor.constructorid
                ).values('raceid', 'position')

                # 그래프 데이터 생성
                year_position_map = {race['year']: None for race in selected_races}  # 초기화

                for result in results:
                    for race in selected_races:
                        if result['raceid'] == race['raceid']:
                            year_position_map[race['year']] = result['position']
                            break

                # 그래프용 라벨 및 데이터 생성 (출전한 연도만 포함)
                graph_labels = sorted([year for year, position in year_position_map.items() if position is not None])
                graph_data = [year_position_map[year] for year in graph_labels]

    # Debug: 그래프 데이터 출력
    print("Graph Labels:", graph_labels)  # 그래프 X축 라벨(연도)
    print("Graph Data:", graph_data)  # 그래프 Y축 데이터(순위)

    context = {
        'search_type': search_type,
        'query': query,
        'suggestions': suggestions,
        'circuits': circuits,
        'graph_labels': graph_labels,
        'graph_data': graph_data,
    }
    return render(request, 'apps/F1_Search.html', context)

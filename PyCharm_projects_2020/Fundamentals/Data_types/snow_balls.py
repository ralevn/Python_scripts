N = int(input()) # Number of snow balls

max_quality = 0

for i in range(N):
    snow_ball_snow = int(input())
    snow_ball_time = int(input())
    snow_ball_value = int(input())
    snow_ball_quality = (snow_ball_snow / snow_ball_time) ** snow_ball_value
    if N == 0:
        max_quality = snow_ball_quality
    else:
        if snow_ball_quality >= max_quality:
            max_quality = int (snow_ball_quality)
            max_snow = snow_ball_snow
            max_time = snow_ball_time
            max_value = snow_ball_value

print(f'{max_snow} : {max_time} = {max_quality} ({max_value})')
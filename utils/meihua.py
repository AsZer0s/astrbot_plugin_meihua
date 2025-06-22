from datetime import datetime

# 根据当前时间（时辰）起卦
def generate_hexagram_by_time():
    now = datetime.now()
    hour = now.hour
    base_trigram = hour % 8  # 得到一个三爻卦（乾=0，兑=1...坤=7）
    changing_line = (hour // 3) % 6  # 变爻位置
    return generate_full_hexagram(base_trigram, changing_line)

# 根据三数起卦法生成卦象
def generate_hexagram_by_numbers(num1, num2, num3):
    total = num1 + num2 + num3
    base = total % 8
    changing_line = total % 6
    return generate_full_hexagram(base, changing_line)

# 卦名映射
def trigram_name(index):
    names = ["乾", "兑", "离", "震", "巽", "坎", "艮", "坤"]
    return names[index]

# 生成完整的六爻卦
def generate_full_hexagram(base, changing_line):
    upper_trigram = (base + 1) % 8  # 上卦
    lower_trigram = base  # 下卦
    hexagram_number = base * 8 + upper_trigram + 1  # 六十四卦编号
    hexagram_name = get_hexagram_name(hexagram_number)
    interpretation = get_interpretation(hexagram_number)
    
    return (
        f"本卦：{trigram_name(lower_trigram)}上 {trigram_name(upper_trigram)}下 ({hexagram_name})\n"
        f"变爻：第{changing_line + 1}爻\n"
        f"解释：{interpretation}"
    )

# 获取六十四卦名称
def get_hexagram_name(number):
    hexagrams = {
        1: "乾为天", 2: "坤为地", 3: "水雷屯", 4: "山水蒙",
        5: "水天需", 6: "天水讼", 7: "地水师", 8: "水地比",
        # ... 补充剩余六十四卦名称
    }
    return hexagrams.get(number, "未知卦")

# 获取卦象解释
def get_interpretation(number):
    interpretations = {
        1: "元亨利贞。初九：潜龙勿用。",
        2: "元亨。利牝马之贞。",
        # ... 补充剩余六十四卦解释
    }
    return interpretations.get(number, "暂无解释")
